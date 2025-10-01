"""
Variables locales y globales en las funciones en Python

LOCAL: Variable definida dentro de una función y solo se puede usar dentro de esa función.

GLOBAL: Variable definida fuera de cualquier función y se puede usar en cualquier parte del código, incluyendo dentro de funciones.

"""

# Variable Global
cita = "Ni los genios son tan genios, ni los mediocres son tan mediocres"
# Es accesible desde cualquier parte del código

print(cita)

def imprimirCita():
    # Variable Local
    cita = "Solo los genios pueden cambiar de opinión"
    # Si comentamos la línea anterior, se usará la variable global que tiene el mismo nombre.
    print(cita)

    year = 2025
    print(year)

    global website # Declarar que se usará la variable global dentro de la función
    website = "manrio.dev"
    print(f"Dentro de la función: {website}")

imprimirCita()
print(f"Fuera de la función: {website}")

# print(year)  # Error, la variable year no existe fuera de la función, ya que es una variable local.

