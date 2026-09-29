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

def similitud_jaccard(pelicula1, pelicula2):
    g1 = catalogo[pelicula1]
    g2 = catalogo[pelicula2]
    interseccion = len (g1 & g2)
    union = len(g1 | g2)
    return interseccion / union

pares = [
    ("Inception", "The Matrix"),
    ("Inception","Titanic"),
    ("Toy Story","Shreck"),
    ("The Godfather","Jhon Wick"),
]
for p1,p2 in pares:
    sim = similitud_jaccard(p1,p2)
    print(f"Similitud entre {p1} y {p2} es {sim*100}%")
