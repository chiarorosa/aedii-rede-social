"""Testes do ranking de engajamento ordenado por Merge Sort."""

import unittest

from py.ordenacao import gerar_ranking


class TestOrdenacaoRanking(unittest.TestCase):
    """Confirma cálculo de engajamento, empate e usuários sem atividade."""

    def test_calcula_engajamento_e_desempata_por_usuario(self):
        """Em empate, @ana deve preceder @bruno alfabeticamente."""
        usuarios = [
            ["1", "@bruno", "Bruno", "2025-01-01"],
            ["2", "@ana", "Ana", "2025-01-01"],
            ["3", "@caio", "Caio", "2025-01-01"],
        ]
        seguidores = [["1", "2"]]
        posts = [["1", "1", "2025-01-01", "2", "x"]]

        ranking = gerar_ranking(usuarios, seguidores, posts)

        self.assertEqual(ranking[0], [1, 2, "@ana", "Ana", 2])
        self.assertEqual(ranking[1], [2, 1, "@bruno", "Bruno", 2])
        self.assertEqual(ranking[2], [3, 3, "@caio", "Caio", 0])

    def test_soma_curtidas_e_seguidores_para_formar_engajamento(self):
        """A fórmula é seguidores vezes dois mais curtidas dos posts."""
        usuarios = [
            ["1", "@ana", "Ana", "2025-01-01"],
            ["2", "@bia", "Bia", "2025-01-01"],
        ]
        seguidores = [["1", "2"], ["1", "2"], ["2", "1"]]
        posts = [
            ["1", "2", "2025-01-01", "5", "x"],
            ["2", "2", "2025-01-02", "3", "y"],
        ]

        ranking = gerar_ranking(usuarios, seguidores, posts)

        self.assertEqual(ranking[0], [1, 2, "@bia", "Bia", 12])
        self.assertEqual(ranking[1], [2, 1, "@ana", "Ana", 2])


if __name__ == "__main__":
    unittest.main()
