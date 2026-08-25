class Nodo:
    def __init__(self, titulo, artista, duracion):
        self.titulo = titulo
        self.artista = artista
        self.duracion = duracion

class Cancion:
    def __init__(self, cancion):
        self.cancion = cancion
        self.siguiente = None
        self.anterior = None

class lista_canciones:
    def __init__(Self):
        self.cabeza = None

    def agregar_cancion(self, titulo, artista, duracion):
        nueva_cancion = cancion (Sornero, Blessd, 151)
        nuevo_nodo = Nodo(nueva_cancion)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else: