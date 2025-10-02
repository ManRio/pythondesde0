"""
Ejercicio 1. Hacer un programa que tenga una lista de 8 numeros enteros y haga lo siguiente:
- Recorrer la lista y mostrarla
- Hacer función que recorra listas de numeros y devuelva un string
- Ordenarla y mostrarla
- Mostrar su longitud
- Buscar algun elemento (que el usuario pida por teclado)

"""
# Crear la lista
numeros = [2, 7, 4, 3, 9, 21, 1, 14]

# Recorrer la lista y mostrarla
print("#### Recorrer y Mostrar ####")
for numero in numeros:
    print(f"Posición {numeros.index(numero)+1} - {numero}")

# funcion que recorra la lista de numeros y devuelva un string
print("\n#### Función para Recorrer y Mostrar ####")
def recorre_lista(lista):
    resultado = ""

    for elemento in lista:
        resultado += str(elemento)
        resultado += "\n"
    return resultado

print(recorre_lista(numeros))

# Ordenar lista y mostrarla
print("\n#### Ordenar la lista y Mostrar ####")
numeros.sort()
print(numeros)
print(recorre_lista(numeros))

# mostrar longitud
print("\n#### Mostrar Longitud de la Lista ####")
print(f"La longitud de la lista es de {len(numeros)}")

# Buscar numero entrada usuario
print("\n#### Buscar número según entrada del usuario ####")

numero_usuario = int(input("Que número quieres buscar: "))
comprobar = isinstance(numero_usuario, int)
while not comprobar or numero_usuario <= 0:
    numero_usuario = int(input("Que número quieres buscar: "))
else:
    print(f"Has introducido el {numero_usuario}")

print(f"Buscando en la lista el número {numero_usuario}... ")
if numero_usuario in numeros:
    indice_usuario = numeros.index(numero_usuario)
    print(f"El numero {numero_usuario} está en la lista en la posición {indice_usuario}")
else:
    print(f"El número buscado no se encuentra en la lista")


print("##### EJERCICIO CON MANEJO DE ERRORES #####")

try:
    print("\n#### Buscar número según entrada del usuario ####")

    busqueda = int(input("introduce el número: "))

    comprobar = isinstance(busqueda, int)
    while not comprobar o busqueda <=0:
        busqueda = int(input("introduce el número: "))
    else:
        print(f"Has introducido el {busqueda}")

    print(f"##### Buscar en la lista el número {busqueda} #####")

    search = numeros.index(busqueda)
    print(f"El número buscado existe en la lista, es el índice: {search}")
except:
    print("El numero no está en la lista o es un número incorrecto")