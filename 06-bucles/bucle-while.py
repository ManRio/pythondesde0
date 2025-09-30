"""
# BUCLE WHILE
Estructura de control que itera o repite la ejecucion de una serie de instrucciones
tantas veces como sea necesario hasta que una condicion deje de cumplirse.

while condicion:
    bloque de instrucciones
    actualizacion de contador


"""

contador = 1
while contador <= 10:
    print(f"El contador es: {contador}")
    contador += 1  # contador = contador + 1

# Ejemplo

print("##### EJEMPLO #######")

numero_usuario = int(input("¿De que número quieres la tabla de multiplicar?: "))

if numero_usuario < 1:
    numero_usuario = 1

print(f"### Tabla de multiplicar del {numero_usuario} ###")

contador = 1
while contador <= 10:
    print(f"{numero_usuario} x {contador} = {numero_usuario * contador}")
    contador += 1
else:
    print("Tabla finalizada")

print("Programa finalizado")

