class Node:
    """Objeto Nodo para imprementação de lista ou pilha"""

    def __init__(self, value):
        self.valor = value
        self.next = None


class NodeTree:
    """Objeto nodo para implementação de árvores"""

    def __init__(self, value=None):
        self.valor = value
        self.dir = None
        self.esq = None

    def set(self, no):
        """Inicializa o nodo com a referencia de outro nodo"""
        if no:
            self.valor = no.valor
            self.dir = no.dir
            self.esq = no.esq
