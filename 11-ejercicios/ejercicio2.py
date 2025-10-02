"""
EJERCICIO 2.
Escribir un programa que añada valores a una lista mientras que su longitud sea menor a 120
y luego mostrar la lista.
Plus: Usar While y For

"""

coleccion = []

contador = 0


for contador in range(0,120):
    coleccion.append(f"elemento - {contador}")
    print("Mostrando el: " + coleccion[contador])

print(coleccion)


# Con el bucle while

coleccion2 = []
x = 0

while x < 120:
    coleccion2.append(f"elemento - {x}")
    print("Mostrando el: " + coleccion2[x])
    x += 1

print(coleccion2)