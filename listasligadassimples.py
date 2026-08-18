class Node:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class lista:
    def __init__(self):
        self.cabeza = None
    def __agregar_nodo__(self, dato):
        nuevo_nodo = Node(dato)
        if self.cabeza == None:
            self.cabeza = nueno_nodo
        else:
            actual = self.cabeza
            while actual.siguiente !=None:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
        print("Nodo agregado")
    def __mostrar_lista__(self):
        actual = self.cabeza
        if actual != None:
            while actual != None:
                print(f"{actual.dato} -->")
                actual = actual.siguiente
                print("FIN")
        else:
            print("Lista Vacia")
    
    def __metodo_insertar_inicio(self, dato):
        nuevo_nodo = Node(dato)
        nodo_inicio = self.cabeza
        self.cabeza = nodo_inicio
        print("Nodo insertado")

lista_ligada = lista()
lista_ligada.agregar_nodo("Primer Nodo")
lista_ligada.agregar_nodo("Segundo Nodo")
lista_ligada.agregar_nodo(6)
lista_ligada.__mostrar_lista__()                      