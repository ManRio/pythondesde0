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


# Añadir elementos a lista
peliculas[1] = "Gran Torino" # Asigna al indice 1 del array peliculas un nuevo valor
print(peliculas)

cantantes.append("Kase 0") #Con el metodo append añadimos nuevos elementos a las listas
print(cantantes)

# Recorrer y Mostrar una lista
nueva_pelicula = ""
while nueva_pelicula != "parar":
    nueva_pelicula = input("introduce la nueva pelicula: ")
    if nueva_pelicula != "parar":
        peliculas.append(nueva_pelicula)

print("\n********** LISTADO DE PELICULAS **********")
for pelicula in peliculas:
    print(f"{peliculas.index(pelicula)+1} - {pelicula}")


# Listas Multidimensionales (Listas que contienen otras listas)

print("/n### Listado de Contactos ###")

contactos = [
    [
        "Antonio",
        "antonio@antonio.com"
    ],
    [
        "Luis",
        "luis@luis.com"
    ],
    [
        "Salvador",
        "salvador@salvador.com"
    ],
]

print(contactos[1][1]) #muestra el mail de Luis, segundo elemento de la lista principal y segundo elemento de la sublista
print("\n")

for contacto in contactos:
    print(contacto[0]) # Saca los nombres de todos los contactos
print("\n")

for contacto in contactos:
    for elemento in contacto:
        print(elemento)
    print("\n") # Mostrará cada lista dentro de la lista principal, en este caso, nombre y mail

for contacto in contactos:
    for elemento in contacto:
        if contacto.index(elemento) == 0:
            print("Nombre: " + elemento)
        else:
            print("Email: " + elemento)
    print("\n")