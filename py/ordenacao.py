"""Cálculo e ordenação do ranking de engajamento."""


def gerar_ranking(usuarios, seguidores, posts):
    """Calcula e ordena todos os usuários pelo engajamento.

    O engajamento é seguidores vezes dois mais a soma das curtidas dos posts.
    A função usa vetores indexados pelo ID e Merge Sort próprio. O custo é
    O(U + E + P + U log U).
    """
    total_usuarios = len(usuarios)
    seguidores_por_id = [0] * (total_usuarios + 1)
    curtidas_por_id = [0] * (total_usuarios + 1)

    for conexao in seguidores:
        seguido = int(conexao[1])
        seguidores_por_id[seguido] += 1

    for post in posts:
        autor = int(post[1])
        curtidas_por_id[autor] += int(post[3])

    registros = []
    for usuario in usuarios:
        identificador = int(usuario[0])
        engajamento = seguidores_por_id[identificador] * 2
        engajamento += curtidas_por_id[identificador]
        registros.append([identificador, usuario[1], usuario[2], engajamento])

    ordenados = _merge_sort(registros)
    ranking = []
    posicao = 1
    for registro in ordenados:
        ranking.append(
            [posicao, registro[0], registro[1], registro[2], registro[3]]
        )
        posicao += 1
    return ranking


def _merge_sort(registros):
    """Ordena registros por Merge Sort sem usar a ordenação da linguagem."""
    if len(registros) <= 1:
        return registros

    meio = len(registros) // 2
    esquerda = _merge_sort(registros[:meio])
    direita = _merge_sort(registros[meio:])
    return _intercalar(esquerda, direita)


def _intercalar(esquerda, direita):
    """Combina duas listas já ordenadas segundo a regra do ranking."""
    resultado = []
    indice_esquerda = 0
    indice_direita = 0

    while indice_esquerda < len(esquerda) and indice_direita < len(direita):
        if _vem_antes(esquerda[indice_esquerda], direita[indice_direita]):
            resultado.append(esquerda[indice_esquerda])
            indice_esquerda += 1
        else:
            resultado.append(direita[indice_direita])
            indice_direita += 1

    while indice_esquerda < len(esquerda):
        resultado.append(esquerda[indice_esquerda])
        indice_esquerda += 1

    while indice_direita < len(direita):
        resultado.append(direita[indice_direita])
        indice_direita += 1

    return resultado


def _vem_antes(primeiro, segundo):
    """Define maior engajamento e, no empate, menor @usuario como melhor."""
    if primeiro[3] != segundo[3]:
        return primeiro[3] > segundo[3]
    return primeiro[1] < segundo[1]
