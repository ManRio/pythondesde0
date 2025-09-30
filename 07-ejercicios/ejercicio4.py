"""
Ejercicio 4.
    Pedir dos números al usuario y hacer todas las operaciones básicas de una calculadora y mostrarlo por pantalla.

"""

print("Calculadora básica")
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2 if num2 != 0 else "Indefinida (no se puede dividir por cero)"

print("### Resultados ###")
print(f"Suma: {num1} + {num2} = {suma}")
print(f"Resta: {num1} - {num2} = {resta}")
print(f"Multiplicación: {num1} * {num2} = {multiplicacion}")
print(f"División: {num1} / {num2} = {division}")

print("##################")
# Fin del programa
