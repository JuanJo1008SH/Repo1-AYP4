class Comando:
    def __init__ (self,dispositivo, hora, accion):
        self.dispositivo = dispositivo
        self.hora = hora
        self.accion = accion
        self.siguiente = None
class Automatizacion:
    def __init__(self):
        self.cabeza = None

    def agregar_comando(self, dispositivo, hora, accion):
        nuevo_Comando = Comando(dispositivo, hora, accion)
        nuevo_Comando.siguiente = self.cabeza
        self.cabeza = nuevo_Comando

    def contar_apagados(self):
        return self.contar_apagados_recursivo(self.cabeza)
    def contar_apagados_recursivo(self, actual):
        if actual.accion == "apagar":
            return 1 + self.contar_apagados_recursivo(actual.siguiente)
        else:
            return 0 + self.contar_apagados_recursivo(actual.siguiente)
    def cancelar_eventos(self, hora_limite):
        self.cabeza = self.cancelar_recursivo(self.cabeza, hora_limite)
    def cancelar_recursivo(self, actual, hora_limite):
        if actual == None:
            return None
        if actual.hora < hora_limite:
            return self.cancelar_recursivo(actual.siguiente, hora_limite)
        actual.siguiente = self.cancelar_recursivo(actual.siguiente, hora_limite)
        return actual

        