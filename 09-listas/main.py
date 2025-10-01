"""
LISTAS (arrays)
Son colecciones o conjuntos de datos/valores, bajo un unico nombre.
Para acceder a esos valores, usamos un indice numerico.

"""

pelicula = "Batman"

# Como definir una lista
peliculas = ["Batman", "Spiderman", "El señor de los anillos"]
cantantes = list(("2pac", "Drake", "Jenni Rivera"))
years = list(range(2000, 2026))
variada = ["Juan", 45, True, 12.34]
print(peliculas)
print(cantantes)
print(years)
print(variada)

#indices
print(peliculas[1]) # Saca el elemento con indice 1 en esa lista
print(peliculas[-2]) # con numeros negativos comenzaria a contar desde atrás, siendo -1 el último valor de la lista, y en este caso sacaria el segundo elemento empezando por el final
print(cantantes[0:2]) # Saca una sublista en el rango de indices indicados
print(cantantes[1:]) # Saca todos los elementos A PARTIR del índice indicado

peliculas[1] = "Gran Torino" # Asigna al indice 1 del array peliculas un nuevo valor
print(peliculas)
