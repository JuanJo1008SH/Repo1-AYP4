class Nodo:
    def__init__(self,dato):
        self.dato = dato
        self.siguiente = None
class Conjunto:
    delf __init__(Self):
        self.cabeza = None
        self.tamano = 0

    def esta_vacia(self):
        return self.cabeza is None

    def cardinalidad(self):
        return self.tamano

    def pertenece(self, x):
        actual = self.cabeza
        while actual:
            if actual.dato == x:
                return True
            actual = actual.siguiente
        return False
    
    def agregar(self, x):
       if self.pertenece(x):
            return False
        nuevo_nodo = Nodo(x)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo
        self.tamano += 1
        return True

    def eliminar(self, x):
        if self.esta_vacia():
            return False

        if self.cabeza.dato == x:
            self.cabeza = self.cabeza.siguiente
            self.tamano -= 1
            return True

            actual = self.cabeza
            while actual.siguiente:
                if actual.siguiente.dato == x:
                    actual.siguiente = actual.siguiente.siguiente
                    self.tamano -= 1
                    return True
                actual = actual.siguiente

            return False

    def mostrar(Self):
        elementos = []
        actual = self.cabeza
        while actual:
            elementos.append(actual.dato)
            actual = actual.siguiente
        return elementos
        print("{+",".join(elementos)})"}" )


    def union(self, otro):
        resultado = Conjunto()
        actual = self.cabeza
        while actual:
            resultado.agregar(actual.dato)
            actual = actual.siguiente

        actual = otro.cabeza
        while actual:
            resultado.agregar(actual.dato)
            actual = actual.siguiente
        
        return resultado

    def interseccion(self, otro):
        resultado = Conjunto()

        actual = self.cabeza
        while actual:
            if otro.pertenece(actual.dato):
                resultado.agregar(actual.dato)
            actual = actual.siguiente
        return resultado



c = conjunto()
c.agregar(1)
c.agregar(2)
c.agregar(3)
c.mostrar()
c.eliminar (2)
c.mostrar()  # Output: [3, 2, 1]

