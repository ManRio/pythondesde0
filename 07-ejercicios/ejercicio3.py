"""
Ejercicio 3.
    Escribir un script que muestre por pantalla todos los cuadrados
    (un número multiplicado por sí mismo) de los 60 primeros números
    naturales (del 1 al 60). Resolverlo con for y con While.

"""

# Con for

for numero in range(1, 61):
    cuadrado2 = numero * numero
    print(f"El cuadrado de {numero} es {cuadrado2}")

# Con While
numero = 1
while numero <= 60:
    cuadrado = numero * numero
    print(f"El cuadrado de {numero} es {cuadrado}")
    numero += 1


