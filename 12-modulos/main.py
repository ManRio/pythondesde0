"""
MODULOS:
Son funcionalidades ya hechas para reutilizar.
En python hay muchos moduilos, que los puedes consultar aqui
https://docs.python.org/3/py-modindex.html

Podemos conseguir modulos que ya vienen en el lenguaje, modulos en internet y crear nuestros
propios modulos.
"""
# Import modulo propio
import mimodulo # Importamos todo el modulo

print(mimodulo.holaMundo("Manuel Rios"))
print(mimodulo.calculadora(3, 5))

# podemos importar una sola funcion de la siguiente forma
from mimodulo import holaMundo

# de esta forma a la hora de llamar a la funcion no es necesario poner delante el nombre del modulo
print(holaMundo("Viejo Sabroso!"))

# Para importar todo el contenido del modulo y poder llamar a las funciones sin tener que poner delante el nombredelmodulo.funcion() lo podemos hacer de la siguiente forma:
#from mimodulo import *
# ¡CUIDADO! porque lo importa [Todo] y si algo no lo usas te avisará el lint de vsCode


# Modulo de Fechas

import datetime

print(datetime.date.today())

fecha_completa = datetime.datetime.now()
print(fecha_completa)

print(fecha_completa.year)
print(fecha_completa.month)
print(fecha_completa.day)

# En la documentación aparecen todos los metodos que contiene este modulo
fecha_personalizada = fecha_completa.strftime("%d/%m/%Y")
print(f"Mi fecha personalizada", fecha_personalizada)

# Modulo Matematicas

import math

print("Raiz cuadrada de 10: ", math.sqrt(10))
print("Numero pi: ", math.pi)

print("Redondear al alza : ", math.ceil(6.7865934))
print("Redondear a la baja: ", math.floor(6.54321))

# Modulo Random
import random

print ("Numero aleatorio entre 16 y 67: ", random.randint(15, 67))
