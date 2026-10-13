"""
===============================================================================
    PLANTILLAS MAESTRAS - LISTAS ENLAZADAS (RECURSIÓN) Y CONJUNTOS
===============================================================================
Uso: Reemplazar 'Elemento' por la clase del examen (ej. Paciente, Pedido).
Reemplazar 'prioridad' o 'valor' por el atributo a evaluar (ej. urgencia, edad).
"""

class Elemento:
    def __init__(self, nombre, valor, prioridad, estado=False):
        self.nombre = nombre
        self.valor = valor
        self.prioridad = prioridad
        self.estado = estado
        self.siguiente = None

class ListaGenerica:
    def __init__(self):
        self.cabeza = None

    # =========================================================================
    # PLANTILLA 1: INSERTAR ORDENADO (Mayor a Menor) - RECURSIVO
    # Sirve para: Agregar pacientes por urgencia, rankings, colas de prioridad.
    # =========================================================================
    def agregar_ordenado(self, nombre, valor, prioridad):
        nuevo = Elemento(nombre, valor, prioridad)
        self.cabeza = self._agregar_recursivo(self.cabeza, nuevo)

    def _agregar_recursivo(self, actual, nuevo):
        # CASO BASE: Final de lista O encontramos la posición (mayor va antes)
        # NOTA: Cambiar el '>' por '<' si piden ordenar de menor a mayor.
        if actual is None or nuevo.prioridad > actual.prioridad:
            nuevo.siguiente = actual
            return nuevo
        
        # CASO RECURSIVO: Avanzar al siguiente nodo
        actual.siguiente = self._agregar_recursivo(actual.siguiente, nuevo)
        return actual


    # =========================================================================
    # PLANTILLA 2: CONTAR O SUMAR CON CONDICIÓN - RECURSIVO
    # Sirve para: Contar pacientes críticos, sumar valores de pedidos pendientes.
    # =========================================================================
    def contar_condicional(self):
        return self._contar_recursivo(self.cabeza)

    def _contar_recursivo(self, actual):
        if actual is None:
            return 0
        
        # CAMBIAR CONDICIÓN AQUÍ SEGÚN EL EXAMEN (Ej: urgencia >= 4 y no atendido)
        # Si piden SUMAR en vez de contar, cambiar el '1' por 'actual.valor'
        cumple = 1 if (actual.prioridad >= 4 and not actual.estado) else 0
        
        return cumple + self._contar_recursivo(actual.siguiente)


    # =========================================================================
    # PLANTILLA 3: FILTRAR Y CREAR NUEVA LISTA - RECURSIVO
    # Sirve para: Filtrar mayores de edad, extraer pedidos de un cliente.
    # =========================================================================
    def filtrar_elementos(self, limite):
        nueva_lista = ListaGenerica()
        nueva_lista.cabeza = self._filtrar_recursivo(self.cabeza, limite)
        return nueva_lista

    def _filtrar_recursivo(self, actual, limite):
        if actual is None:
            return None
        
        # CAMBIAR CONDICIÓN AQUÍ SEGÚN EL EXAMEN (Ej: actual.edad >= limite)
        if actual.valor >= limite:
            # 1. Crear clon exacto del nodo para no dañar lista original
            copia = Elemento(actual.nombre, actual.valor, actual.prioridad, actual.estado)
            # 2. Enganchar el clon al resultado del resto de la lista
            copia.siguiente = self._filtrar_recursivo(actual.siguiente, limite)
            return copia
        else:
            # Si no cumple, ignorar este nodo y pasar directamente al siguiente
            return self._filtrar_recursivo(actual.siguiente, limite)


# =============================================================================
# PLANTILLA 4: MACHETE RÁPIDO DE CONJUNTOS (SETS)
# =============================================================================
def operaciones_conjuntos(lista1, lista2):
    # Convertir a conjuntos
    c1 = set(lista1)
    c2 = set(lista2)
    
    # 1. Eliminar duplicados de una lista y saber si todos son únicos
    sin_duplicados = list(c1)
    es_unica = len(c1) == len(lista1)  # Retorna True si no había repetidos
    
    # 2. Operaciones matemáticas
    interseccion = c1 & c2    # Elementos en AMBOS (los que se repiten en las dos)
    diferencia = c1 - c2      # Elementos en c1 que NO están en c2
    union = c1 | c2           # Juntar ambos sin repetidos
    subconjunto = c1.issubset(c2) # True si todo c1 está dentro de c2


# =============================================================================
# PLANTILLA 5: MACHETE DE MEMOIZACIÓN (Optimización recursiva)
# =============================================================================
MEMO = {}
def recursivo_optimizado(n):
    # 1. Casos base
    if n <= 1: return n
    
    # 2. Retornar si ya está guardado
    if n in MEMO:
        return MEMO[n]
    
    # 3. Calcular, GUARDAR y luego retornar
    MEMO[n] = recursivo_optimizado(n-1) + recursivo_optimizado(n-2)
    return MEMO[n]