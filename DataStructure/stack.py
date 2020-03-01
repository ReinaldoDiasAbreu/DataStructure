from DataStructure.node import Node


class Stack:
    """Stack - Last In First Out"""

    def __init__(self):
        self.top = None
        self._size = 0

    def push(self, elem):
        """Insere do elem no topo da pilha."""
        no = self.top
        self.top = Node(elem)
        self.top.next = no
        self._size = self._size + 1

    def pop(self):
        """Remove e retorna elemento do topo da pilha."""
        if self._size > 0:
            no = self.top
            self.top = self.top.next
            self._size = self._size - 1
            return no.valor
        raise IndexError("The stack is empty!")

    def peek(self):
        """Retorna valor do topo da pilha."""
        if self._size > 0:
            return self.top.valor
        raise IndexError("The stack is empty!")

    def __len__(self):
        """Retorna o numero de elementos da pilha."""
        return self._size

    def __repr__(self):
        """Imprime a pilha."""
        rep = ""
        p = self.top
        while p:
            rep += str(p.valor)
            if p.next:
                rep += " -> "
            p = p.next
        return rep

    def __str__(self):
        return self.__repr__()
