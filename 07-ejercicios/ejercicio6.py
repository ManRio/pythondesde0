"""
Ejercicio 6.

Mostrar todas las tablas de multiplicar del 1 al 10.
Mostrando el titulo de cada tabla y después los resultados de la tabla.

"""

print("Tablas de multiplicar del 1 al 10")

for i in range(1, 11):
    print(f"\n### Tabla del {i} ###")
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")
print("\nFin de las tablas de multiplicar.")
