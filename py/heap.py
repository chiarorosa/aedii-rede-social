"""Implementação manual de uma heap de máximo."""


class HeapMaxima:
    """Guarda itens priorizados em uma heap de máximo baseada em lista.

    Cada item deve ter o formato ``[prioridade, chave_desempate, valor]``.
    A maior prioridade é removida primeiro. Em empate, a menor chave de
    desempate é considerada melhor.
    """

    def __init__(self):
        """Cria uma heap vazia com a posição zero sem uso."""
        self.itens = [None]

    def esta_vazia(self):
        """Retorna ``True`` quando não há elementos na heap. O(1)."""
        return len(self.itens) == 1

    def inserir(self, item):
        """Insere um item e restaura a propriedade da heap. O(log n)."""
        self.itens.append(item)
        self._subir(len(self.itens) - 1)

    def remover_maximo(self):
        """Remove e retorna o melhor item da heap, ou ``None`` se vazia.

        A remoção troca a raiz pelo último item e o desloca para baixo,
        quando necessário. A complexidade é O(log n).
        """
        if self.esta_vazia():
            return None

        melhor = self.itens[1]
        ultimo = self.itens.pop()
        if not self.esta_vazia():
            self.itens[1] = ultimo
            self._descer(1)
        return melhor

    def _tem_prioridade_maior(self, primeiro, segundo):
        """Indica se ``primeiro`` deve aparecer antes de ``segundo``."""
        if primeiro[0] != segundo[0]:
            return primeiro[0] > segundo[0]
        return primeiro[1] < segundo[1]

    def _subir(self, indice):
        """Move um item para cima até sua posição correta na heap."""
        while indice > 1:
            pai = indice // 2
            if not self._tem_prioridade_maior(self.itens[indice], self.itens[pai]):
                return
            self.itens[indice], self.itens[pai] = self.itens[pai], self.itens[indice]
            indice = pai

    def _descer(self, indice):
        """Move um item para baixo até sua posição correta na heap."""
        while indice * 2 < len(self.itens):
            filho_esquerdo = indice * 2
            filho_direito = filho_esquerdo + 1
            melhor_filho = filho_esquerdo

            if (
                filho_direito < len(self.itens)
                and self._tem_prioridade_maior(
                    self.itens[filho_direito], self.itens[filho_esquerdo]
                )
            ):
                melhor_filho = filho_direito

            if not self._tem_prioridade_maior(
                self.itens[melhor_filho], self.itens[indice]
            ):
                return

            self.itens[indice], self.itens[melhor_filho] = (
                self.itens[melhor_filho],
                self.itens[indice],
            )
            indice = melhor_filho
