class Paciente:
    def __init__(self, nombre, edad, urgencia, atendido=False):
        self.nombre = nombre
        self.edad = edad
        self.urgencia = urgencia  # 1=baja, 5=crítica
        self.atendido = atendido
        self.siguiente = None

    def __str__(self):
        estado = "✓" if self.atendido else "○"
        return f"[{estado}] {self.nombre} (edad:{self.edad}) - Urgencia:{self.urgencia}"


class ListaPacientes:
    def __init__(self):
        self.cabeza = None

    def mostrar(self):
        actual = self.cabeza
        if actual is None:
            print(" Sin pacientes")
            return
        while actual:
            print(f" {actual}")
            actual = actual.siguiente

    # 1. Agregar paciente ordenado por urgencia - RECURSIVO ──
    def agregar(self, nombre, edad, urgencia):
        nuevo = Paciente(nombre, edad, urgencia)
        self.cabeza = self._agregar_recursivo(self.cabeza, nuevo)

    def _agregar_recursivo(self, actual, nuevo):
        # Caso base: Llegamos al final O la urgencia del nuevo es estrictamente mayor que la de 'actual'
        if actual is None or nuevo.urgencia > actual.urgencia:
            nuevo.siguiente = actual
            return nuevo
        
        # Caso recursivo: Si la urgencia es menor o igual, avanzamos al siguiente nodo
Aquí tienes el código completo y listo para copiar y pegar en tu examen:

```python
class Paciente:
    def __init__(self, nombre, edad, urgencia, atendido=False):
        self.nombre = nombre
        self.edad = edad
        self.urgencia = urgencia  # 1=baja, 5=crítica
        self.atendido = atendido
        self.siguiente = None

    def __str__(self):
        estado = "✓" if self.atendido else "○"
        return f"[{estado}] {self.nombre} (edad:{self.edad}) - Urgencia:{self.urgencia}"


class ListaPacientes:
    def __init__(self):
        self.cabeza = None

    def mostrar(self):
        actual = self.cabeza
        if actual is None:
            print(" Sin pacientes")
            return
        while actual:
            print(f" {actual}")
            actual = actual.siguiente

    # Agregar paciente ordenado por urgencia - RECURSIVO
    def agregar(self, nombre, edad, urgencia):
        nuevo = Paciente(nombre, edad, urgencia)
        self.cabeza = self._agregar_recursivo(self.cabeza, nuevo)

    def _agregar_recursivo(self, actual, nuevo):
        if actual is None or nuevo.urgencia > actual.urgencia:
            nuevo.siguiente = actual
            return nuevo
        actual.siguiente = self._agregar_recursivo(actual.siguiente, nuevo)
        return actual

    # Contar pacientes críticos - RECURSIVO
    def contar_criticos(self):
        return self._contar_criticos_recursivo(self.cabeza)

    def _contar_criticos_recursivo(self, actual):
        if actual is None:
            return 0
        cumple = 1 if (actual.urgencia >= 4 and not actual.atendido) else 0
        return cumple + self._contar_criticos_recursivo(actual.siguiente)

    # Filtrar por edad - RECURSIVO
    def filtrar_mayores(self, edad_minima):
        nueva = ListaPacientes()
        nueva.cabeza = self._filtrar_mayores_recursivo(self.cabeza, edad_minima)
        return nueva

    def _filtrar_mayores_recursivo(self, actual, edad_minima):
        if actual is None:
            return None
        if actual.edad >= edad_minima:
            copia = Paciente(actual.nombre, actual.edad, actual.urgencia, actual.atendido)
            copia.siguiente = self._filtrar_mayores_recursivo(actual.siguiente, edad_minima)
            return copia
        return self._filtrar_mayores_recursivo(actual.siguiente, edad_minima)