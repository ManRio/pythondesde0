nombre = "Manuel Rios"

print(nombre) # Imprime el valor de la variable nombre
print(type(nombre)) # Imprime el tipo de dato de la variable nombre

# Detectar el tipado
comprobar = isinstance(nombre, str) # Devuelve True si la variable nombre es de tipo str
if comprobar:
    print("La variable es una cadena de texto")
else:
    print("La variable no es una cadena de texto")

# limpiar espacios
frase = "   mi Contenido   "
print(frase)
print(frase.strip()) # Elimina los espacios en blanco al inicio y al final de la cadena
print(frase.lstrip()) # Elimina los espacios en blanco al inicio de la cadena
print(frase.rstrip()) # Elimina los espacios en blanco al final de la cadena
print(frase.replace("mi", "tu")) # Reemplaza una palabra por otra en la cadena
print(frase.split()) # Convierte la cadena en una lista, separando por espacios
print(frase.lower()) # Convierte la cadena a minúsculas
print(frase.upper()) # Convierte la cadena a mayúsculas
print(len(frase)) # Devuelve la longitud de la cadena
print(frase.capitalize()) # Convierte la primera letra de la cadena a mayúscula
print(frase.count("o")) # Cuenta cuantas veces aparece una letra en la cadena
print(frase.startswith("mi")) # Devuelve True si la cadena empieza por la palabra indicada
print(frase.endswith("contenido")) # Devuelve True si la cadena termina por la palabra indicada
print(frase.find("Contenido")) # Devuelve la posición de la primera letra de la palabra indicada
print(frase.index("Contenido")) # Devuelve la posición de la primera letra de la palabra indicada, si no la encuentra da error
print(frase.isnumeric()) # Devuelve True si la cadena es un número
print(frase.isalpha()) # Devuelve True si la cadena es solo letras
print(frase.isalnum()) # Devuelve True si la cadena es letras y números
print(frase.title()) # Convierte la primera letra de cada palabra a mayúscula
print(frase.zfill(50)) # Rellena la cadena con ceros a la izquierda hasta completar el número de caracteres indicado
print(frase.center(50)) # Centra la cadena en el espacio indicado, rellenando con espacios a la izquierda y derecha
print(frase.center(50, "*")) # Centra la cadena en el espacio indicado, rellenando con el carácter indicado a la izquierda y derecha
print(frase.ljust(50, "-")) # Alinea la cadena a la izquierda en el espacio indicado, rellenando con el carácter indicado a la derecha
print(frase.rjust(50, "-")) # Alinea la cadena a la derecha
print(frase.swapcase()) # Invierte las mayúsculas y minúsculas de la cadena
print(frase.encode()) # Codifica la cadena en bytes
print(frase.endswith("Contenido")) # Devuelve True si la cadena termina por la palabra indicada
print(frase.isprintable()) # Devuelve True si la cadena es imprimible
print(frase.isspace()) # Devuelve True si la cadena es solo espacios en blanco
print(frase.partition("Contenido")) # Devuelve una tupla con tres elementos: la parte antes de la palabra indicada, la palabra indicada y la parte después de la palabra indicada
print(frase.rpartition("Contenido")) # Devuelve una tupla con tres elementos: la parte antes de la palabra indicada, la palabra indicada y la parte después de la palabra indicada, buscando desde el final
print(frase.splitlines()) # Convierte la cadena en una lista, separando por saltos de línea
print(frase.translate(str.maketrans("m", "M"))) # Reemplaza caracteres según el diccionario indicado
print(frase.removeprefix("   ")) # Elimina el prefijo indicado de la cadena
print(frase.removesuffix("   ")) # Elimina el sufijo indicado de la cadena
print(frase.isidentifier()) # Devuelve True si la cadena es un identificador válido
print(frase.isdecimal()) # Devuelve True si la cadena es un número decimal
print(frase.isdigit()) # Devuelve True si la cadena es un número
print(frase.islower()) # Devuelve True si la cadena está en minúsculas
print(frase.isupper()) # Devuelve True si la cadena está en mayúsculas
print(frase.istitle()) # Devuelve True si la cadena está en formato título
print(frase.casefold()) # Convierte la cadena a minúsculas, similar a lower pero más agresivo
print(frase.expandtabs()) # Reemplaza los tabuladores por espacios
