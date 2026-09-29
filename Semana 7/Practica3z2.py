

# A. Convertir lista a conjunto (elimina duplicados automáticamente)
numeros = [1, 2, 2, 3, 4, 4]
conjunto = set(numeros)  # {1, 2, 3, 4}

# B. Verificar si una fila NO tiene elementos repetidos (Unicidad)
# Si el tamaño del set es igual al tamaño de la lista, son todos únicos.
def es_unica(lista):
    return len(set(lista)) == len(lista)  # Retorna True o False

# C. Validar contra un conjunto de referencia (Ej: Sudoku)
OBJETIVO = {1, 2, 3, 4, 5, 6, 7, 8, 9}

def validar_fila_matriz(matriz, num_fila):
    fila = matriz[num_fila]
    return set(fila) == OBJETIVO

# D. Recorrer una columna en una matriz (3x3 o NxN)
def obtener_columna(matriz, num_columna):
    columna = []
    for i in range(len(matriz)):
        columna.append(matriz[i][num_columna])
    return set(columna) == OBJETIVO

# E. Recorrer un subcuadro 3x3 en una matriz
def obtener_subcuadro(matriz, fila_inicio, col_inicio):
    subcuadro = []
    for i in range(3):
        for j in range(3):
            subcuadro.append(matriz[fila_inicio + i][col_inicio + j])
    return set(subcuadro) == OBJETIVO



class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class Conjunto:
    def __init__(self):
        self.cabeza = None

    # PATRÓN SAGRADO 1: Recorrido estándar (Pertenece / Pertenece a la lista)
    def pertenece(self, x):
        actual = self.cabeza
        while actual:  # Mientras no sea None
            if actual.dato == x:
                return True
            actual = actual.siguiente  # ¡PASO OBLIGATORIO PARA AVANZAR!
        return False



# A. SUBCOMJUNTO (A ⊆ B): ¿Todos los elementos de A están en B?
def es_subconjunto(conjunto_a, conjunto_b):
    actual = conjunto_a.cabeza
    while actual:
        if not conjunto_b.pertenece(actual.dato):
            return False  # Si uno solo de A no está en B, ya no es subconjunto
        actual = actual.siguiente
    return True  # Si recorrió todo A sin fallar, es True

# B. VERIFICAR PERMISOS DE USUARIO
# Permisos requeridos debe ser subconjunto de los permisos que tiene el usuario
def tiene_permisos(permisos_usuario, permisos_requeridos):
    return es_subconjunto(permisos_requeridos, permisos_usuario)

# C. DIFERENCIA (A - B): Elementos que están en A pero NO en B
def diferencia(conjunto_a, conjunto_b):
    resultado = []
    actual = conjunto_a.cabeza
    while actual:
        if not conjunto_b.pertenece(actual.dato):
            resultado.append(actual.dato)
        actual = actual.siguiente
    return resultado

# D. INTERSECCIÓN (A ∩ B): Elementos que están en AMBOS conjuntos
def interseccion(conjunto_a, conjunto_b):
    resultado = []
    actual = conjunto_a.cabeza
    while actual:
        if conjunto_b.pertenece(actual.dato):
            resultado.append(actual.dato)
        actual = actual.siguiente
    return resultado
