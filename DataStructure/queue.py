from DataStructure.node import Node


class Queue:
    """Chained Queue - First In First Out"""

    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def push(self, elem):
        """Insere do elemento na fila."""
        no = Node(elem)
        if self.tail is None:
            self.tail = no
        else:
            self.tail.next = no
            self.tail = no

        if self.head is None:
            self.head = no

        self._size = self._size + 1

    def pop(self):
        """Remove elemento da fila."""
        if self._size > 0:
            valor = self.head.valor
            self.head = self.head.next
            self._size = self._size - 1
            return valor
        raise IndexError("The queue is empty!")

    def peek(self):
        """Retorna primeiro valor da fila."""
        if self._size > 0:
            return self.head.valor
        raise IndexError("The queue is empty!")

    def __len__(self):
        """Retorna o numero de elementos da fila."""
        return self._size

    def __repr__(self):
        """Imprime a fila."""
        rep = ""
        p = self.head
        while p:
            rep += str(p.valor)
            if p.next:
                rep += " -> "
            p = p.next
        return rep
