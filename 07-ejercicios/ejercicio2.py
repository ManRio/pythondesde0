"""
Ejercicio 2: Escribir un script que nos muestre por pantalla todos los numeros pares del 1 al 120.

"""

for numero in range(1, 121):
    if numero % 2 == 0:
        print(numero)

# Otra forma de hacerlo
for numero in range(2, 121, 2):
    print(numero)

# Otra forma de hacerlo
for numero in range(1, 121):
    if not numero % 2:
        print(numero)


