# Para trabajar con directorios debemos utilizar el módulo os
import os
import shutil

# crear carpeta
if not os.path.isdir("./mi_carpeta"):
    os.mkdir("./mi_carpeta")
else:
    print("ya existe el directorio")

# Copiar o Mover una carpeta
"""
ruta_original = "./mi_carpeta"
ruta_nueva = "./mi_carpeta_COPIADA"
# Debemos realizarlo con shutil ya que os no tiene funciones para ello
shutil.copytree(ruta_original, ruta_nueva)

# Eliminar una carpeta
os.rmdir('./mi_carpeta_COPIADA')

"""

# Listar archivos
print("Contenido de mi carpeta: ")
contenido = os.listdir("./mi_carpeta")

for fichero in contenido:
    print("Fichero: "+fichero)