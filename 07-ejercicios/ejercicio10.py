"""
Ejercicio 10. El programa tienen que pedir la nota de 15 alumnos y decir cuantos han aprobado y cuantos han suspendido

"""

notas = {"aprobados": 0, "suspendidos": 0}
for i in range(15):
    nota = float(input(f"Introduce la nota del alumno {i + 1}: "))
    if nota >= 5:
        notas["aprobados"] += 1
    else:
        notas["suspendidos"] += 1
print(f"Han aprobado {notas['aprobados']} alumnos y han suspendido {notas['suspendidos']} alumnos")


