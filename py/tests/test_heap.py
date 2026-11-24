"""Testes de comportamento da heap de máximo."""

import unittest

from py.heap import HeapMaxima


class TestHeapMaxima(unittest.TestCase):
    """Garante a prioridade e o desempate da heap própria."""

    def test_remove_por_prioridade_e_desempate_alfabetico(self):
        """Uma prioridade maior vence; em empate, a menor chave vence."""
        heap = HeapMaxima()
        heap.inserir([2, "@bruno", 2])
        heap.inserir([2, "@ana", 3])
        heap.inserir([3, "@caio", 4])

        self.assertEqual(heap.remover_maximo(), [3, "@caio", 4])
        self.assertEqual(heap.remover_maximo(), [2, "@ana", 3])
        self.assertEqual(heap.remover_maximo(), [2, "@bruno", 2])

    def test_remover_de_heap_vazia_retorna_none(self):
        """Uma heap vazia não deve tentar acessar um elemento inexistente."""
        self.assertIsNone(HeapMaxima().remover_maximo())


if __name__ == "__main__":
    unittest.main()
