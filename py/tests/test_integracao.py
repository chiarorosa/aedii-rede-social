"""Testes das validações e mensagens usadas pelo menu."""

import io
import os
import sys
import unittest
from contextlib import redirect_stdout

PASTA_PY = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PASTA_PY not in sys.path:
    sys.path.insert(0, PASTA_PY)

from avl import ArvoreAVLPosts
from grafo import GrafoSeguidores
from main import (
    data_valida,
    mostrar_posts_entre,
    mostrar_sugestoes,
    validar_quantidade,
)


class TestIntegracaoMenu(unittest.TestCase):
    """Confirma entradas inválidas e mensagens das opções do terminal."""

    def test_valida_datas_reais_e_quantidades_positivas(self):
        """Datas impossíveis e quantidades não positivas devem ser recusadas."""
        self.assertTrue(data_valida("2025-01-01"))
        self.assertFalse(data_valida("2025-13-01"))
        self.assertFalse(data_valida("2025-02-29"))
        self.assertEqual(validar_quantidade("3"), 3)
        self.assertIsNone(validar_quantidade("0"))
        self.assertIsNone(validar_quantidade("abc"))

    def test_mostra_usuario_inexistente_na_sugestao(self):
        """A opção de sugestão deve informar quando o @usuario não existe."""
        usuarios = [["1", "@ana", "Ana", "2025-01-01"]]
        grafo = GrafoSeguidores(1, [])
        saida = io.StringIO()

        with redirect_stdout(saida):
            mostrar_sugestoes(grafo, usuarios, "@ausente", 2)

        self.assertIn("Usuário não encontrado.", saida.getvalue())

    def test_recusa_intervalo_de_datas_invertido(self):
        """A tela não consulta a AVL quando a data inicial é posterior à final."""
        arvore = ArvoreAVLPosts()
        saida = io.StringIO()

        with redirect_stdout(saida):
            mostrar_posts_entre(arvore, "2025-03-02", "2025-03-01")

        self.assertIn("Data inicial não pode ser maior que a data final.", saida.getvalue())


if __name__ == "__main__":
    unittest.main()
