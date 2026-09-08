class Pagina:
    def __init__(self, url,  titulo, tiempo):
        self.url = url
        self.titulo = titulo
        self.tiempo = tiempo
        self.siguiente = None
class Historial:
    def __init__(self):
        self.cabeza = None

    def visitar(self, url, titulo, tiempo):
        nueva_pagina = Pagina(url, titulo, tiempo)
        nueva_pagina.siguiente = self.cabeza
        self.cabeza = nueva_pagina

    def tiempo_total(self):
        return self.tiempo_total_recursivo(self.cabeza)
    
    def tiempo_total_recursivo(self,actual):
        if actual == None:
            return 0
        return actual.tiempo + self.tiempo_total_recursivo(actual.siguiente)
    def buscar_Por_dominio(self, texto):
        nueva_lista = Historial()
        self.buscar_recursivo(self.cabeza, texto, nueva_lista)
        return nueva_lista
    def buscar_recursivo(self, actual, texto, nueva_lista):
        if actual == None:
            return
        if texto in actual.url:
            nueva_lista.visitar(actual.url, actual.titulo, actual.tiempo)
        self.buscar_recursivo(actual.siguiente, texto, nueva_lista)

    def eliminar_rapidas(self, tiempo_limite):
        self.cabeza = self.eliminar_recursivo(self.cabeza, tiempo_limite)
    def eliminar_recursivo(self, actual, tiempo_limite):
        if actual == None:
            return None
        if actual.tiempo < tiempo_limite:
            return self.eliminar_recursivo(actual.siguiente, tiempo_limite)
        actual.siguiente = self.eliminar_recursivo(actual.siguiente, tiempo_limite)
        return actual
