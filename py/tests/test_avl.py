"""Testes da árvore AVL usada para indexar posts por data."""

import unittest

from py.avl import ArvoreAVLPosts


def post(numero, data, texto="post"):
    """Cria um post pequeno no mesmo formato do CSV da atividade."""
    return [str(numero), "1", data, "0", texto]


class TestArvoreAVLPosts(unittest.TestCase):
    """Verifica balanceamento e consulta cronológica por intervalo."""

    def test_rotacoes_deixam_a_data_central_na_raiz(self):
        """As quatro configurações de três chaves devem ser balanceadas."""
        sequencias = [
            ["2025-03-03", "2025-03-02", "2025-03-01"],
            ["2025-03-01", "2025-03-02", "2025-03-03"],
            ["2025-03-03", "2025-03-01", "2025-03-02"],
            ["2025-03-01", "2025-03-03", "2025-03-02"],
        ]

        for sequencia in sequencias:
            arvore = ArvoreAVLPosts()
            for numero, data in enumerate(sequencia, start=1):
                arvore.inserir(post(numero, data))
            self.assertEqual(arvore.raiz.data, "2025-03-02")

    def test_busca_intervalo_inclui_limites_e_ordem_cronologica(self):
        """A busca deve trazer as duas datas-limite em ordem crescente."""
        arvore = ArvoreAVLPosts()
        for numero, data in enumerate(
            ["2025-03-03", "2025-03-01", "2025-03-02", "2025-03-04"],
            start=1,
        ):
            arvore.inserir(post(numero, data))

        encontrados = arvore.buscar_intervalo("2025-03-01", "2025-03-03")
        self.assertEqual(
            [registro[2] for registro in encontrados],
            ["2025-03-01", "2025-03-02", "2025-03-03"],
        )

    def test_mantem_todos_os_posts_da_mesma_data_na_ordem_de_insercao(self):
        """Posts da mesma chave ficam juntos sem que um substitua o outro."""
        arvore = ArvoreAVLPosts()
        arvore.inserir(post(1, "2025-03-01", "primeiro"))
        arvore.inserir(post(2, "2025-03-01", "segundo"))

        encontrados = arvore.buscar_intervalo("2025-03-01", "2025-03-01")
        self.assertEqual([registro[4] for registro in encontrados], ["primeiro", "segundo"])

    def test_retorna_lista_vazia_quando_nao_ha_posts_no_intervalo(self):
        """Um período sem chaves na árvore resulta em uma lista vazia."""
        arvore = ArvoreAVLPosts()
        arvore.inserir(post(1, "2025-03-10"))

        self.assertEqual(arvore.buscar_intervalo("2025-03-01", "2025-03-09"), [])


if __name__ == "__main__":
    unittest.main()
