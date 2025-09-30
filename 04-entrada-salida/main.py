# Entrada

nombre = input("¿Cómo te llamas? ")
# Todo lo que se recoge por input() es tipo str (cadena de texto)
edad = int(input("¿Cuántos años tienes? "))  # Convertir a entero



# Salida

print("Hola " + nombre)
print(f"Hola {nombre}")  # Usando f-string (Python 3.6+)
print("Hola me llamo {}".format(nombre))  # Usando format (Python 3+)

# Salida concatenada

print("Hola " + nombre + ", tienes " + str(edad) + " años.")
print(f"Hola {nombre}, tienes {edad} años.")  # Usando f-string (Python 3.6+)
print("Hola me llamo {} y tengo {} años.".format(nombre, edad))  # Usando format (Python 3+)


