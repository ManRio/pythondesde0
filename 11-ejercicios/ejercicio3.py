"""
EJERCICIO 3.
Programa que compruebe si una variable está vacía y si está vacía, rellenarla con texto en minúsculas y mostrarlo en mayúsculas.

"""

texto = ""

if len(texto) == 0:
    print("La variable está vacía")
    texto = "abcde"
    print(texto.upper())
else:
    print(f"La variable NO está vacía, contiene lo siguiente: {texto}")