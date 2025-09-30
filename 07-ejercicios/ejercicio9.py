"""
Ejercicio9: Hacer un programa que pida numeros al usuario indefinidamente
hasta que ingrese el numero 111

"""

contador = 0

while True:
    numero = int(input("Introduce un numero: "))
    if numero == 111:
        break
    contador += 1
print(f"Has introducido {contador} numeros")

