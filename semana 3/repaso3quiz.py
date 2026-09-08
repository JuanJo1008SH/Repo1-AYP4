class Commit:
    def _init__(self, id_commit, mensaje, lineas_modificadas):
        self.id_commit = id_commit
        self.mensaje = mensaje
        self.lineas_modificadas = lineas_modificadas
        self.siguiente = None
class Repositorio:
    def __init__ (self):
        self.cabeza = None
    def hacer_commit(self, id_commit, mensaje, lineas_modificadas):
        nuevo_commit = Commit(id_commit, mensaje, lineas_modificadas)
        nuevo_commit.siguiente = self.cabeza
        self.cabeza = nuevo_commit
    def total_lineas_modificadas(self):
        return self. total_lineas_modificadas_recursivo(self.cabeza)
    def total_lineas_modificadas_recursivo(self, actual):
        if actual == None:
            return 0
        return actual.lineas_modificadas + self.total_lineas_modificadas_recursivo(actual.siguiente)