elemento = 5
lista = [5, 6, 7, 8, 9]
if elemento in lista:
    print("Está en la lista")

conjunto = {5, 4, 3, 2, 1}

if elemento in conjunto:
    print("Está en el conjunto")

conjunto = set(lista)
print(conjunto)
conjunto.add(8)
conjunto.discard(9)
conjunto.pop()
for num in conjunto:
    print(num)


