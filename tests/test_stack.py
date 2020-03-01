from DataStructure.stack import Stack

if __name__ == "__main__":
    pilha = Stack()
    pilha.push(10)
    pilha.push(20)
    pilha.push(30)
    print(pilha.peek())
    print(len(pilha))
    print(pilha)
    pilha.pop()
    print(len(pilha))
    print(pilha)
