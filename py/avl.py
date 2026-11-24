"""Árvore AVL para consultar posts por intervalo de datas."""


class NoAVL:
    """Representa uma data, seus posts e seus dois filhos na árvore AVL."""

    def __init__(self, post):
        """Cria um nó cuja chave é a data na posição dois do post."""
        self.data = post[2]
        self.posts = [post]
        self.esquerda = None
        self.direita = None
        self.altura = 1


class ArvoreAVLPosts:
    """Mantém posts balanceados por data para buscas de intervalo rápidas."""

    def __init__(self):
        """Cria uma árvore AVL inicialmente vazia."""
        self.raiz = None

    def inserir(self, post):
        """Insere um post, agrupando os que possuem a mesma data. O(log d)."""
        self.raiz = self._inserir(self.raiz, post)

    def buscar_intervalo(self, data_inicial, data_final):
        """Lista os posts entre duas datas, inclusive, em ordem cronológica.

        A travessia evita ramos que não podem conter datas do intervalo.
        Sua complexidade é O(log d + p), sendo p o total de posts devolvidos.
        """
        if data_inicial > data_final:
            return []
        encontrados = []
        self._buscar_intervalo(self.raiz, data_inicial, data_final, encontrados)
        return encontrados

    def _inserir(self, no, post):
        """Insere recursivamente e devolve a raiz rebalanceada do trecho."""
        if no is None:
            return NoAVL(post)

        data = post[2]
        if data < no.data:
            no.esquerda = self._inserir(no.esquerda, post)
        elif data > no.data:
            no.direita = self._inserir(no.direita, post)
        else:
            no.posts.append(post)
            return no

        self._atualizar_altura(no)
        return self._rebalancear(no)

    def _buscar_intervalo(self, no, data_inicial, data_final, encontrados):
        """Percorre apenas os ramos cuja chave pode estar no intervalo."""
        if no is None:
            return

        if no.data > data_inicial:
            self._buscar_intervalo(no.esquerda, data_inicial, data_final, encontrados)

        if data_inicial <= no.data <= data_final:
            for post in no.posts:
                encontrados.append(post)

        if no.data < data_final:
            self._buscar_intervalo(no.direita, data_inicial, data_final, encontrados)

    def _altura(self, no):
        """Retorna a altura de um nó, considerando zero para filho ausente."""
        if no is None:
            return 0
        return no.altura

    def _atualizar_altura(self, no):
        """Atualiza a altura de um nó usando a maior altura de seus filhos."""
        altura_esquerda = self._altura(no.esquerda)
        altura_direita = self._altura(no.direita)
        no.altura = 1 + max(altura_esquerda, altura_direita)

    def _fator_balanceamento(self, no):
        """Calcula altura esquerda menos altura direita de um nó."""
        if no is None:
            return 0
        return self._altura(no.esquerda) - self._altura(no.direita)

    def _rotacao_direita(self, no):
        """Rotaciona à direita quando o ramo esquerdo está excessivamente alto."""
        nova_raiz = no.esquerda
        subarvore_transferida = nova_raiz.direita

        nova_raiz.direita = no
        no.esquerda = subarvore_transferida

        self._atualizar_altura(no)
        self._atualizar_altura(nova_raiz)
        return nova_raiz

    def _rotacao_esquerda(self, no):
        """Rotaciona à esquerda quando o ramo direito está excessivamente alto."""
        nova_raiz = no.direita
        subarvore_transferida = nova_raiz.esquerda

        nova_raiz.esquerda = no
        no.direita = subarvore_transferida

        self._atualizar_altura(no)
        self._atualizar_altura(nova_raiz)
        return nova_raiz

    def _rebalancear(self, no):
        """Aplica uma das quatro rotações AVL quando necessário."""
        fator = self._fator_balanceamento(no)

        if fator > 1:
            if self._fator_balanceamento(no.esquerda) < 0:
                no.esquerda = self._rotacao_esquerda(no.esquerda)
            return self._rotacao_direita(no)

        if fator < -1:
            if self._fator_balanceamento(no.direita) > 0:
                no.direita = self._rotacao_direita(no.direita)
            return self._rotacao_esquerda(no)

        return no
