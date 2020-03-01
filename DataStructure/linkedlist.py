from DataStructure.node import Node


class LinkedList:
    """Linked List"""

    def __init__(self):
        self.head = None
        self._size = 0

    def append(self, elem):
        """Insere elemento no fim da lista."""
        if self.head:
            no = self.head
            while no.next:
                no = no.next
            no.next = Node(elem)
        else:
            self.head = Node(elem)
        self._size = self._size + 1

    def insert(self, index, elem):
        """Insere valor na lista."""
        if index == 0:
            nodo = Node(elem)
            nodo.next = self.head
            self.head = nodo
        else:
            no = self._getnode(index - 1)
            nodo = Node(elem)
            nodo.next = no.next
            no.next = nodo
        self._size = self._size + 1

    def delete(self, index):
        """Remove elemento da lista pelo index."""
        if index == 0:
            self.head = self.head.next
        else:
            noant = self._getnode(index - 1)
            no = self._getnode(index)
            noant.next = no.next
        self._size = self._size - 1

    def remove(self, elem):
        """Remoção do primeiro elemento da lista compatível."""
        if self.head is None:
            raise ValueError("{} is not in list".format(elem))
        elif self.head.valor == elem:
            self.head = self.head.next
            self._size = self._size - 1
            return True
        else:
            ant = self.head
            no = self.head.next
            while no:
                if no.valor == elem:
                    ant.next = no.next
                    no.next = None
                    self._size = self._size - 1
                    return True
                ant = no
                no = no.next

        raise ValueError("{} is not in list".format(elem))

    def __getitem__(self, index):
        """Obtem valor da posição index da lista"""
        no = self._getnode(index)
        if no:
            return no.valor
        raise IndexError("List index out of range")

    def __setitem__(self, index, elem):
        """Altera valor na posição index da lista"""
        no = self._getnode(index)
        if no:
            no.valor = elem
        else:
            raise IndexError("List index out of range")

    def index(self, elem):
        """Retorna o indice do elemento na lista"""
        no = self.head
        i = 0
        while no:
            if no.valor == elem:
                return i
            i = i + 1
            no = no.next
        raise ValueError("Value {} is not in list.".format(elem))

    def _getnode(self, index):
        no = self.head
        if no:
            for i in range(index):
                if no:
                    no = no.next
                else:
                    raise IndexError("List index out of range")
            return no
        else:
            raise IndexError("The list is empty")

    def __len__(self):
        """Retorna o numero de elementos da lista."""
        return self._size

    def __repr__(self):
        """Imprime a lista."""
        rep = "["
        p = self.head
        while (p):
            rep += str(p.valor)
            if p.next:
                rep += " "
            p = p.next
        rep += "]"
        return rep

    def __str__(self):
        return self.__repr__()
