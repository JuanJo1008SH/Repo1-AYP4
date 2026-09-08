class Entrega:
    def __init__(self, cliente, direccion, peso_kg):
        self.cliente = cliente
        self.direccion = direccion
        self.peso_kg = peso_kg
        self.siguiente = None
class Ruta:
    def __init__(self):
        self.cabeza = None
    def agregar_entrega(self, cliente, direccion, peso_kg):
        nueva_entrega = Entrega(cliente, direccion, peso_kg)
        nueva_entrega.siguiente = self.cabeza
        self.cabeza = nueva_entrega
    def peso_Total(self):
        return self.peso_total_recursivo(self.cabeza)
    def peso_total_recursivo(self, actual):
        if actual == None:
            return 0
        return actual.peso_kg + self.peso_total_recursivo(actual.siguiente)
    
    def filtrar_peso(self,peso_minimo):
        nueva_lista = Ruta()
        self.filtrar_recursivo(self.cabeza, peso_minimo, nueva_lista)
        return nueva_lista
    
    def filtrar_recursivo(self, actual, peso_minimo, nueva_lista):
        if nueva_lista == None:
            return 
        if actual.peso_kg > peso_minimo:
            nueva_lista.agregar_entrega(actual.cliente, actual.direccion, actual.peso_kg)
            self.filtrar_recursivo(actual.siguiente, peso_minimo, nueva_lista)
    