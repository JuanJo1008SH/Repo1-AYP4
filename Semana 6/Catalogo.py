catalogo = {
    "inception": {"ciencia ficcion", "accion", "thriller", "drama"},
    "The Matrix": {"ciencia ficcion", "accion", "thriller"},
    "Titanic": {"romance", "drama", "historica"},
    "Avengers": {"ciencia ficcion", "accion", "aventura"},
    "Jhon Wick": {"accion", "thriller", "crimen"},
    "Interstellar": {"ciencia ficcion", "drama", "aventura"},
    "Toy Story": {"animacion", "comedia", "aventura"},
    "Shreck": {"animacion", "comedia", "aventura"},
}

peliculas = list(catalogo.keys())
genero = list(catalogo.values())

for i in range(len(peliculas)):
    for j in range(i + 1, len(peliculas)):
        p1,p2 = peliculas[i], peliculas[j]
        comunes = catalogo[p1] & catalogo[p2]
        if len(comunes)>= 2:
            print(f" {p1} <--> {p2}")
            print(f"Generos en comun: {comunes}")

favoritos = {"accion", "ciencia ficcion", "aventura"}

recomendaciones =[]

for pelicula, generos in catalogo.items():
    coincidencias = generos & favoritos
    if coincidencias:
        puntaje = len(coincidencias) / len(favoritos)
        recomendaciones.append((pelicula, puntaje* 100, coincidencias))
recomendaciones.sort(key=lambda x:x[1], reverse =True)
print(recomendaciones)

todos_los_generos = set()

for generos in catalogo.values():
    todos_los_generos |= generos

print(todos_los_generos)
#Mostrar por genero
for genero in todos_los_generos:
    peliculas_genero = set()
    for pelicula, generos in catalogo.items():
        if genero in generos:
            peliculas_genero.add(pelicula)
    print(f"Genero: {genero} --> Peliculas: {peliculas_genero}")