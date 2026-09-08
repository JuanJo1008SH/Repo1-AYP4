#HACER UN ALGORITMO RECURSIVO QUE SUME LOS DIGITOS DE UN NUMERO
#EJEMPLO 123 1--2--3 1 + 2 + 3 = 6
def sumar_digitos(n):
    if n//10 ==0:
        return n
    return (n%10) + sumar_digitos(n//10)
print(sumar_digitos(456))