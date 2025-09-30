"""
Una variable es un contenedor de información
que dentro guardará un dato, se pueden crear
muchas variables y que cada una guarde un dato distinto.
"""

texto = "Máster en Python"
texto2 = "Con Víctor Robles"
numero = 45
decimal = 6.7
booleano = True

print(texto)
print(texto2)
print(numero)
print(decimal)
print(booleano)


# concatencación de variables
nombre = "Manuel"
apellido = "Ríos"
web = "www.manrio.dev"

print(nombre + " " + apellido + " - " + web)

# No se puede concatenar texto con números
numero = 25
# print(nombre + " " + apellido + " - " + numero)  # Error
print(nombre + " " + apellido + " - " + str(numero))  # Convertir número a texto
print(f"{nombre} {apellido} - {numero}")  # Usando f-string (Python 3.6+)

# metodo format (Python 3+)
print("Hola me llamo {} {} y mi web es {}".format(nombre, apellido, web))

# Saber el tipo de dato de una variable
print(type(texto))
print(type(numero))
print(type(decimal))
print(type(booleano))
print(type(texto2))