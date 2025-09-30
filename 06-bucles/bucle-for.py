"""
#FOR
for variable in elemento iterable (lista, rango, etc):
    #bloque de instrucciones

"""
contador = 0
resultado = 0

for contador in range(0, 5):
    print("Valor actual del contador: ", contador)
    resultado = resultado + contador
    print(f"El resultado es: {resultado}")

print("Fin del bucle")

# Ejemplo con tablas de multiplicar
print("\nTablas de multiplicar")

numero_usuario = int(input("De que numero quieres la tabla? "))
if numero_usuario < 1:
    numero_usuario = 1


print(f"#### Tabla de multiplicar del {numero_usuario} ####")
for numero_tabla in range(1, 11):
    if numero_usuario == 45:
        print("No se pueden mostrar números prohibidos")
        break

    print(f"{numero_usuario} x {numero_tabla} = {numero_usuario * numero_tabla}")

print("#### Fin de la tabla ####")

