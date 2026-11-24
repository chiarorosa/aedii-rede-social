"""Testes de sugestão de usuários pelo grafo de seguidores."""

import unittest

from py.grafo import GrafoSeguidores


class TestGrafoSeguidores(unittest.TestCase):
    """Verifica candidatos, pontuação e casos de borda da sugestão."""

    def setUp(self):
        """Monta uma rede pequena com caminhos de dois passos conhecidos."""
        self.usuarios = [
            ["1", "@ana", "Ana", "2025-01-01"],
            ["2", "@bia", "Bia", "2025-01-01"],
            ["3", "@caio", "Caio", "2025-01-01"],
            ["4", "@duda", "Duda", "2025-01-01"],
            ["5", "@enzo", "Enzo", "2025-01-01"],
            ["6", "@fabi", "Fabi", "2025-01-01"],
        ]
        seguidores = [
            [1, 2], [1, 3], [2, 4], [3, 4], [2, 5], [2, 1], [3, 2]
        ]
        self.grafo = GrafoSeguidores(6, seguidores)

    def test_sugere_ordenado_por_conexoes_em_comum(self):
        """Um candidato alcançado duas vezes deve vir antes do alcançado uma."""
        sugestoes = self.grafo.sugerir("@ana", 5, self.usuarios)

        self.assertEqual(
            sugestoes,
            [[4, "@duda", "Duda", 2], [5, "@enzo", "Enzo", 1]],
        )

    def test_nao_sugere_origem_nem_usuarios_ja_seguidos(self):
        """Caminhos de retorno e usuários seguidos diretamente são excluídos."""
        sugestoes = self.grafo.sugerir("@ana", 5, self.usuarios)
        ids_sugeridos = [sugestao[0] for sugestao in sugestoes]

        self.assertNotIn(1, ids_sugeridos)
        self.assertNotIn(2, ids_sugeridos)
        self.assertNotIn(3, ids_sugeridos)

    def test_retorna_none_para_usuario_inexistente(self):
        """A busca informa claramente que não encontrou o usuário solicitado."""
        self.assertIsNone(self.grafo.sugerir("@inexistente", 1, self.usuarios))

    def test_retorna_lista_vazia_para_usuario_sem_seguidos(self):
        """Sem seguidos diretos não há pessoas a duas conexões de distância."""
        self.assertEqual(self.grafo.sugerir("@fabi", 3, self.usuarios), [])


if __name__ == "__main__":
    unittest.main()
