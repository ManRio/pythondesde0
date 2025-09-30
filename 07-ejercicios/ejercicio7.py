"""
Ejercicio 7: Hacer un programa que muestre los impares entre dos numeros que elija el usuario

"""

numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))

if numero1 < numero2:
    for i in range(numero1, numero2 + 1):
        if i % 2 != 0:
            print(i)
else:
    for i in range(numero2, numero1 + 1):
        if i % 2 != 0:
            print(i)
print("Fin del programa")