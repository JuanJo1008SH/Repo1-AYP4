MATRIZ_TURNOS = [
    ["Carlos", "Ana", "Sofia"],
    ["Pedro", "Ana", "Pedro"],   # Repetido
    ["Lucia", "Mateo", "Elena"]
]

def area_es_valida(matriz, num_area):
    fila_actual=matriz[num_area]
    return len(set(fila_actual)) == len(fila_actual)

def elementos_exclusivos_de_a(conjunto_a, conjunto_b):
    exclusivos = []
    actual = conjunto_a.cabeza
    
    while actual:
        if not conjunto_b.pertenece(actual.dato):
            exclusivos.append(actual.dato)
        actual = actual.siguiente
        
    return exclusivos