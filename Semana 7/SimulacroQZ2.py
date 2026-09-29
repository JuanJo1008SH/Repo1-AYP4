import re

NUMEROS_VALIDOS = {1, 2, 3, 4, 5, 6, 7, 8, 9}

TABLERO = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]
]
def validar_fila(tablero, num_fila):
    fila_actual = tablero[num_fila]
    return set(fila_actual) == NUMEROS_VALIDOS

def validar_columna(tablero, num_columna):
    columna_actual = []
    for i in range(9):
        columna_actual.append(tablero[i][num_columna])
        
    return set(columna_actual) == NUMEROS_VALIDOS

def validar_subcuadro(tablero, fila_inicio, col_inicio):
    subcuadro = []
    for i in range(3):
        for j in range(3):
            # Sumamos la coordenada de inicio más el desplazamiento actual
            numero = tablero[fila_inicio + i][col_inicio + j]
            subcuadro.append(numero)
            
    return set(subcuadro) == NUMEROS_VALIDOS

def es_subconjunto(conjunto_a, conjunto_b):
    # 1. Arrancamos desde el primer nodo de A
    actual = conjunto_a.cabeza
    
    # 2. Recorremos mientras haya nodos
    while actual:
        # 3. Si el dato actual de A NO está en B, entonces no es subconjunto
        if not conjunto_b.pertenece(actual.dato):
            return False
            
        # Pasamos al siguiente nodo de A
        actual = actual.siguiente
        
    # 4. Si terminó el ciclo y no falló ninguna vez, es subconjunto
    return True

def tiene_permisos(permisos_usuario, permisos_requeridos):
    # Un usuario puede actuar si los permisos exigidos son subconjunto de los suyos
    return es_subconjunto(permisos_requeridos, permisos_usuario)