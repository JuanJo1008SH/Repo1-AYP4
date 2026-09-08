class Nodo:
    def __init__(self, titulo, artista, duracion):
        self.titulo = titulo
        self.artista = artista
        self.duracion = duracion
        self.siguiente = None
        self.anterior = None

class Lista_canciones:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def agregar_cancion(self, titulo, artista, duracion):
        if self.cabeza is None:
            self.cabeza = nueva_cancion
            self.cola = nueva_cancion
        else:
            self.cola.siguiente = nueva_cancion
            nueva_cancion.anterior = self.cola
            self.cola = nueva_cancion
    def mostrar_canciones(self):
        if self.cabeza == None:
            print("No hay canciones en la lista.")
            return
        else:
            actual=self.cabeza
            while actual != None:
                print(f"Título: {actual.titulo}, Artista: {actual.artista}, Duración: {actual.duracion}")
                actual=actual.siguiente

    def buscar_cancion(self, nombre_buscado):
        actual = self.cabeza
        while actual != None:
            if actual.titulo == nombre_buscado:
                print(f"¡Canción encontrada!: {actual.titulo} de {actual.artista}")
                return 
                
            actual = actual.siguiente

        print("La canción no está en la playlist.")

    def eliminar_cancion(self, nombre_buscado):
        actual = self.cabeza
        while actual !=None:
            if actual.titulo == nombre_buscado:
                actual=None
                print(f"¡Canción eliminada!: {actual.titulo} de {actual.art