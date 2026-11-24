"""Grafo de seguidores e sugestão de pessoas para seguir."""

try:
    from .heap import HeapMaxima
except ImportError:
    from heap import HeapMaxima


class GrafoSeguidores:
    """Representa as conexões dirigidas por listas de adjacência."""

    def __init__(self, total_usuarios, seguidores):
        """Monta a lista de usuários seguidos por cada ID. O(E)."""
        self.total_usuarios = total_usuarios
        self.adjacencias = []
        for _ in range(total_usuarios + 1):
            self.adjacencias.append([])

        for conexao in seguidores:
            seguidor = int(conexao[0])
            seguido = int(conexao[1])
            self.adjacencias[seguidor].append(seguido)

    def sugerir(self, usuario, quantidade, usuarios):
        """Retorna até ``quantidade`` sugestões para ``usuario``.

        Uma sugestão é alcançada em dois passos no grafo. Usuário de origem
        e pessoas já seguidas diretamente não entram no resultado. O custo é
        O(U + G + C log(C + 1)), em que G são as conexões examinadas e C os
        candidatos distintos.
        """
        origem = self._encontrar_id(usuario, usuarios)
        if origem is None:
            return None
        if quantidade <= 0:
            return []

        usuarios_por_id = [None] * (self.total_usuarios + 1)
        for registro in usuarios:
            usuarios_por_id[int(registro[0])] = registro

        ja_segue = [False] * (self.total_usuarios + 1)
        contagens = [0] * (self.total_usuarios + 1)
        candidatos = []

        for seguido in self.adjacencias[origem]:
            ja_segue[seguido] = True

        for seguido in self.adjacencias[origem]:
            for candidato in self.adjacencias[seguido]:
                if candidato == origem or ja_segue[candidato]:
                    continue
                if contagens[candidato] == 0:
                    candidatos.append(candidato)
                contagens[candidato] += 1

        heap = HeapMaxima()
        for candidato in candidatos:
            registro = usuarios_por_id[candidato]
            heap.inserir([contagens[candidato], registro[1], candidato])

        sugestoes = []
        while len(sugestoes) < quantidade:
            melhor = heap.remover_maximo()
            if melhor is None:
                break
            registro = usuarios_por_id[melhor[2]]
            sugestoes.append([melhor[2], registro[1], registro[2], melhor[0]])
        return sugestoes

    def _encontrar_id(self, usuario, usuarios):
        """Busca linearmente o ID associado a um nome de usuário. O(U)."""
        for registro in usuarios:
            if registro[1] == usuario:
                return int(registro[0])
        return None
