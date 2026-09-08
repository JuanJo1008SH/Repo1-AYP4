#HACER UN ALGORITMO RECURSIVO QUE RECIBA UN STRING Y UN CARACTER
#DEBE DE DEVOLVER EL NUMERO DE VECES QUE EL CARACTER ESTE EN EL STRING
def contar_caracter(palabra, caracter):
    if len(palabra)== 0:
        return 0
    contador = 1 if palabra[0] == caracter else 0
    return contador + contar_caracter(palabra[1:], caracter)
contar_caracter("juanjose", "j")
    