from DataStructure.linkedlist import LinkedList


if __name__ == "__main__":
    lista = LinkedList()
    lista.append(10)
    lista.append(20)
    lista.append(30)
    lista.append(40)
    print(lista)
    lista.insert(1, 15)
    print(lista)
    lista.remove(15)
    print(lista)
    print(lista.index(30))
    print(lista[0])
    lista.delete(0)
    print(lista)
    lista[0] = 50
    print(lista)

