
"""
Ejercicio 5:
Hacer un programa que muestre todos los números entre nos números que diga el usuario.

"""

print("Ingrese dos números y le mostraré todos los números entre ellos.")
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

if num1 < num2:
    for i in range(num1 , (num2 + 1)):
        print(i)
else:
    for i in range(num2, (num1 +1)):
        print(i)
