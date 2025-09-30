"""
Ejercicio 8: ¿Cuanto es el X por ciento de X numero?

"""

numero = float(input("Ingrese un numero: "))
porcentaje = float(input("Ingrese el porcentaje que quiere sacar: "))

resultado = (numero * porcentaje) / 100

print(f"El {porcentaje}% de {numero} es: {resultado}")

print("Fin del programa")
