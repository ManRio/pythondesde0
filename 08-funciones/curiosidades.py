def mi_funcion():
    return "Saludos desde mi función"

def mi_segunda_funcion(nombre):
    return f"Saludos {nombre}"

# Recomendable colocar las funciones al inicio del archivo
# Recomendable que las funciones retornen valores (return) y no usen print dentro de ellas

nombre = "Manuel"
apellidos = "Rios"

print("Hola mundo")
print(f"Bienvenido {nombre} {apellidos}")

mi_funcion()
print(mi_funcion())
print(mi_segunda_funcion("Antonio"))
print(mi_segunda_funcion(nombre))


