from DataStructure.tree import BinarySearchTree
from DataStructure.node import NodeTree


if __name__ == "__main__":
    # Exemplo de uso do objeto BinarySearchTree
    lista = [15, 7, 5, 1, 13, 14, 20, 25, 30]
    a = BinarySearchTree()
    a.insert(10)  # insere um elemento
    a.insert_list(lista)  # insere lista de elementos
    print("Impressão em Ordem: ", a)
    print("Impressão Pré Ordem: ", a.show("rlr"))
    print("Impressão Pós Ordem: ", a.show("lrr"))
    print("Tamanho: ", len(a))
    print("Altura: ", a.height())
    print("Valor Min: {} - Valor Max: {}".format(a.min(), a.max()))
    print("Valor 13 existe? {}".format(a.search(13)))
    print("Valor 22 existe? {}".format(a.search(22)))
    a.remove(10)
    a.remove(15)
    a.remove(1)
    a.remove(20)
    print("Arvore apos remoções: ", a)
    print("Tamanho: ", len(a))
    print("Altura: ", a.height())
    # Criando novo nó
    b = NodeTree()
    # Inserindo referencia da subarvore no nó
    b.set(a.search_node(14))
    # Gerando uma nova arvore a partir do nó
    t = BinarySearchTree(b)
    print("Nova arvore: ", t)
    print("Tamanho nova árvore: ", len(t))
    # Removendo no da nova arvore
    t.remove(14)
    print("Nova arvore após remoção: ", t)
    # Comparando as duas arvores obtidas
    print("Nova Arvore: ", t)
    print("Arvore Anterior: ", a)
