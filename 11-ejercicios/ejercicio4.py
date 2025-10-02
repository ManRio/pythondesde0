"""
Ejercicio 4.
Crear un script que tenga 4 variables, una lista, un string, un entero y un booleano y que imprima un mensaje segun el tipo de dato de cada variable. Usar Funciones

"""
def tipo_var(var):
    if isinstance(var, str):
        print(f"La variable es una cadena y contiene: {var}")
    elif isinstance(var, int):
        print(f"La variable es un número entero y su valor es: {var}")
    elif isinstance(var, list):
        print(f"La variable es una lista y contiene los siguientes elementos: {var}")
    else:
        print(f"La variable es de tipo booleano con tipo {var}")


# Otra forma más efectiva:
def comprobar_tipado(dato, tipo):
    test = isinstance(dato, tipo)
    result = ""

    if test:
        result = f"Esta variable es del tipo {type(dato)} y contiene lo siguiente: {dato}"
    else:
        result = None

    return result

mi_lista = ["rojo", "verde", "azul"]
mi_cadena = "Esta es una cadena de texto"
mi_entero = 38
is_boolean = True

print("\n### Metodo Efectivo ###")
print(comprobar_tipado(mi_lista, list))
print(comprobar_tipado(is_boolean, bool))
print(comprobar_tipado(mi_cadena, str))
print(comprobar_tipado(mi_entero, int))


print("\n### Metodo más 'Rústico' ###")
tipo_var(mi_lista)
tipo_var(is_boolean)
tipo_var(mi_entero)
tipo_var(mi_cadena)