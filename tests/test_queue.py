from DataStructure.queue import Queue


if __name__ == "__main__":
    fila = Queue()
    fila.push(10)
    fila.push(20)
    fila.push(30)
    print(fila)
    print(len(fila))
    print(fila.peek())
    print(fila.pop())
    print(fila)