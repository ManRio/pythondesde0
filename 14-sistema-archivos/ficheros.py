"""
para trabajar con el sistema de archivos en python tenemos que utilizar
el paquete open que está dentro de io
"""

from io import open
import pathlib
import shutil #renombrar, copiar y mover archivos

# Abrir archivo
ruta = str(pathlib.Path().absolute()) + "/fichero_texto.txt" #le indicamos con Pathlib la ruta absoluta y lo guardamos en una variable
archivo = open(ruta, "a+") # Pasamos la ruta indicada anteriormente al archivo, para que lo cree o abra sin error alguno

# Escribir
archivo.write("************* Soy un texto introducido desde Python ***************\n")

# Cerrar Archivo
archivo.close()

# Abrir archivo
ruta = str(pathlib.Path().absolute()) + "/fichero_texto.txt" #le indicamos con Pathlib la ruta absoluta y lo guardamos en una variable
archivo_lectura = open(ruta, "r") # r permiso de lectura

#leer contenido
#contenido = archivo_lectura.read()
#print(contenido)

# Leer contenido y guardarlo en lista
lista = archivo_lectura.readlines()
archivo_lectura.close()

for frase in lista:
    #lista_frase = frase.split()
    #print(lista_frase)
    print("- " + frase)

# Copiar

"""
ruta_original = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
ruta_nueva = str(pathlib.Path().absolute()) + "/fichero_copiado.txt"
shutil.copyfile(ruta_original, ruta_nueva)

"""

# Mover un archivo o Renombrar un archivo

"""
ruta_original = str(pathlib.Path().absolute()) + "/fichero_copiado.txt"
ruta_nueva = str(pathlib.Path().absolute()) + "/fichero_copiado_NUEVO.txt"
shutil.move(ruta_original, ruta_nueva)

"""

# Eliminar un archivo
# Debemos importar el modulo os
"""
import os

ruta_nueva = str(pathlib.Path().absolute()) + "/fichero_copiado_NUEVO.txt"
os.remove(ruta_nueva)

"""

# Comprobar si existe
# Debemos importar os.path
import os.path
ruta_comprobar = os.path.abspath("./") + "/fichero_texto.txt"

if os.path.isfile(ruta_comprobar):
    print("El fichero existe")
else:
    print("Ha habido un error")

