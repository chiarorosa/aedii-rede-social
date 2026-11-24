"""Menu das funcionalidades de sugestão, posts por data e ranking."""

import aedlib

from avl import ArvoreAVLPosts
from grafo import GrafoSeguidores
from ordenacao import gerar_ranking


def data_valida(data):
    """Verifica se uma string está no formato AAAA-MM-DD e representa uma data."""
    if len(data) != 10 or data[4] != "-" or data[7] != "-":
        return False
    if not (data[:4].isdigit() and data[5:7].isdigit() and data[8:].isdigit()):
        return False

    ano = int(data[:4])
    mes = int(data[5:7])
    dia = int(data[8:])
    dias_por_mes = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if mes < 1 or mes > 12:
        return False
    if mes == 2 and (ano % 400 == 0 or (ano % 4 == 0 and ano % 100 != 0)):
        return 1 <= dia <= 29
    return 1 <= dia <= dias_por_mes[mes]


def validar_quantidade(texto):
    """Converte uma quantidade positiva; retorna ``None`` para entrada inválida."""
    if not texto.isdigit():
        return None
    quantidade = int(texto)
    if quantidade <= 0:
        return None
    return quantidade


def mostrar_sugestoes(grafo, usuarios, usuario, quantidade):
    """Imprime as recomendações encontradas para um usuário."""
    sugestoes = grafo.sugerir(usuario, quantidade, usuarios)
    if sugestoes is None:
        print("Usuário não encontrado.")
        return
    if len(sugestoes) == 0:
        print("Não há sugestões para este usuário.")
        return

    print(f"Sugestões para {usuario}:")
    for sugestao in sugestoes:
        print(
            f"{sugestao[1]} - {sugestao[2]} "
            f"({sugestao[3]} conexões em comum)"
        )


def mostrar_posts_entre(arvore, data_inicial, data_final):
    """Imprime posts no intervalo válido e informa o total encontrado."""
    if not data_valida(data_inicial) or not data_valida(data_final):
        print("Data inválida. Use o formato AAAA-MM-DD.")
        return
    if data_inicial > data_final:
        print("Data inicial não pode ser maior que a data final.")
        return

    posts = arvore.buscar_intervalo(data_inicial, data_final)
    for post in posts:
        print(f"{post[2]} | autor {post[1]} | {post[4]}")
    print(f"Total de posts encontrados: {len(posts)}")


def mostrar_ranking(ranking):
    """Imprime até os vinte primeiros usuários do ranking calculado."""
    limite = 20
    if len(ranking) < limite:
        limite = len(ranking)

    print("Ranking de engajamento:")
    for indice in range(limite):
        registro = ranking[indice]
        print(
            f"{registro[0]}º - {registro[2]} ({registro[3]}): "
            f"{registro[4]} pontos"
        )


def construir_avl(posts):
    """Insere todos os posts carregados na árvore AVL uma única vez."""
    arvore = ArvoreAVLPosts()
    for post in posts:
        arvore.inserir(post)
    return arvore


def mostrar_menu():
    """Exibe as opções que correspondem aos três itens deste integrante."""
    print("\n1 - Sugerir usuários")
    print("2 - Posts entre datas")
    print("3 - Ranking de engajamento")
    print("0 - Sair")


def main():
    """Carrega os dados, prepara as estruturas e executa o menu interativo."""
    usuarios, seguidores, posts = aedlib.social_carregar_dados()
    grafo = GrafoSeguidores(len(usuarios), seguidores)
    arvore = construir_avl(posts)
    ranking = gerar_ranking(usuarios, seguidores, posts)

    print(f"Usuários carregados:  {len(usuarios)}")
    print(f"Conexões carregadas:  {len(seguidores)}")
    print(f"Posts carregados:     {len(posts)}")

    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "0":
            print("Programa encerrado.")
            return
        if opcao == "1":
            usuario = input("Digite o @usuario: ").strip()
            quantidade = validar_quantidade(input("Quantidade de sugestões: ").strip())
            if quantidade is None:
                print("A quantidade deve ser um número inteiro positivo.")
            else:
                mostrar_sugestoes(grafo, usuarios, usuario, quantidade)
        elif opcao == "2":
            data_inicial = input("Data inicial (AAAA-MM-DD): ").strip()
            data_final = input("Data final (AAAA-MM-DD): ").strip()
            mostrar_posts_entre(arvore, data_inicial, data_final)
        elif opcao == "3":
            mostrar_ranking(ranking)
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()
