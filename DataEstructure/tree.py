from node import NodeTree

class BinarySearchTree:
    """Arvore Binária de Busca"""

    def __init__(self, no=None):
        if no:
            self.raiz = no
            self._size = self.__reset_size(no)
        else:
            self.raiz = None
            self._size = 0
    
    def insert(self, valor):
        """Insere valor na árvore binária"""
        pai = None
        no = self.raiz
        while(no):
            pai = no
            if valor <= pai.valor:
                no = pai.esq
            else:
                no = pai.dir
        if pai is None:
            self.raiz = NodeTree(valor)
        elif valor <= pai.valor:
            pai.esq = NodeTree(valor) 
        else:
            pai.dir = NodeTree(valor)
        self.__increment()
    
    def insert_list(self, list):
        """Insere lista de valores na árvore"""
        for v in list:
            self.insert(v)

    def search(self, valor):
        """Busca se existe o valor na árvore binária, retorna True se encontrado"""
        pai = None
        no = self.raiz
        while(no):
            pai = no
            if valor == pai.valor:
                return True
            elif valor < pai.valor:
                no = pai.esq
            else:
                no = pai.dir
        return False
    
    def search_node(self, valor):
        """Busca se existe o valor na árvore binária, retorna o nodo se encontrado"""
        no = self.raiz
        while(no):
            if valor == no.valor:
                return no
            elif valor < no.valor:
                no = no.esq
            else:
                no = no.dir
        return None
    
    def __search_node_father(self, valor):
        """Busca se existe o valor na árvore binária, retorna o nodo pai se encontrado"""
        pai = self.raiz
        no = self.raiz
        while(no):
            if valor == no.valor:
                return no, pai
            elif valor < no.valor:
                pai = no
                no = pai.esq
            else:
                pai = no
                no = pai.dir
        return None, None

    def __search_node_max_esq(self, no):
        """Busca o maior valor na árvore binária pela esquerda do nó"""
        if no.dir:
            no = self.__search_node_max_esq(no.dir)
        return no
    
    def __search_node_min_dir(self, no):
        """Busca o menor valor na árvore binária pela esquerda do nó"""
        if no.esq:
            no = self.__search_node_min_dir(no.esq)
        return no
    
    def show(self, type=""):
        """Retorna a representação da árvore na ordem desejada. Default: InOrder"""
        return self.__show(self.raiz, type)

    def __show(self, no, type):
        rep = ""
        if no:
            type = type.lower()
            if type == "rlr":
                # pré-ordem
                rep += self.__pre_order_show(no)
            elif type == "lrr":
                # pós-ordem
                rep += self.__pos_order_show(no)
            else:
                # Em ordem
                rep += self.__in_order_show(no)
        return rep

    def __in_order_show(self, no):
        rep = ""
        if no.esq:
            rep += self.__in_order_show(no.esq)
        rep += ("{} ".format(no.valor))
        if no.dir:
            rep += self.__in_order_show(no.dir)
        return rep
    
    def __pre_order_show(self, no):
        rep = ""
        rep += ("{} ".format(no.valor))
        if no.esq:
            rep += self.__pre_order_show(no.esq)
        if no.dir:
            rep += self.__pre_order_show(no.dir)
        return rep
    
    def __pos_order_show(self, no):
        rep = ""
        if no.esq:
            rep += self.__pos_order_show(no.esq)
        if no.dir:
            rep += self.__pos_order_show(no.dir)
        rep += ("{} ".format(no.valor))
        return rep

    def height(self, no=None):
        """Retorna a altura da árvore"""
        if no == None:
            no = self.raiz
        hesq = 0
        hdir = 0
        if no:
            if no.esq:
                hesq = self.height(no.esq)
            if no.dir:
                hdir = self.height(no.dir)
            if hesq >= hdir:
                return hesq + 1
            else:
                return hdir + 1
        return 0
        
    def remove(self, valor=None):
        if valor:
            nodo, father = self.__search_node_father(valor)
            if nodo and father:
                if nodo.dir == None and nodo.esq == None:
                    # caso folha
                    if(nodo == father):
                        self.raiz = None
                    elif(father.dir and father.dir.valor == valor):
                        father.dir = None
                    elif(father.esq and father.esq.valor == valor):
                        father.esq = None
                    self.__decrement()
                    
                elif (nodo.dir and nodo.esq == None):
                    # caso nodo raiz com filho a direita
                    if(father.dir and father.dir.valor == valor):
                        father.dir = nodo.dir
                    elif(father.esq and father.esq.valor == valor):
                        father.esq = nodo.dir
                    self.__decrement()

                elif (nodo.dir==None and nodo.esq):
                    # caso nodo raiz com filho a esquerda
                    if(father.dir and father.dir.valor == valor):
                        father.dir = nodo.esq
                    elif(father.esq and father.esq.valor == valor):
                        father.esq = nodo.esq
                    self.__decrement()
                
                else:
                    # caso nodo raiz com 2 filhos
                    if(nodo.esq):
                        # Sobre o nó mais a direira da sub esquerda
                        no = self.__search_node_max_esq(nodo.esq)
                        aux = no.valor
                        self.remove(aux)
                        nodo.valor = aux
                    else:
                        # Sobre o nó mais a esquerda da sub direita
                        no = self.__search_node_min_dir(nodo.dir)
                        aux = no.valor
                        self.remove(aux)
                        nodo.valor = aux

    def size(self):
        """Retorna o número de elementos inseridos na árvore"""
        return self._size

    def __increment(self):
        self._size = self._size + 1

    def __decrement(self):
        self._size = self._size - 1

    def __reset_size(self, no):
        cont = 0
        if no.esq:
            cont += self.__reset_size(no.esq)
        cont += 1
        if no.dir:
            cont += self.__reset_size(no.dir)
        return cont

    def min(self):
        """Retorna o menor valor armazenado"""
        no = self.raiz
        if no:
            no = self.__search_node_min_dir(no)
            if no:
                return no.valor
        return None
    
    def max(self):
        """Retorna o maior valor armazenado"""
        no = self.raiz
        if no:
            no = self.__search_node_max_esq(no)
            if no:
                return no.valor
        return None

    def __len__(self):
        return self.size()
    
    def __repr__(self):
        return self.show()
    
    def __str__(self):
        return self.__repr__()
    