
"""
FUNCIONES:
Una función es un conjunto de instrucciones agrupadas bajo un nombre concreto
que pueden reutilizarse invocándolas desde otras partes del código tantas veces como sea necesario.

def nombre_de_mi_funcion(parametro1, parametro2):
    instrucciones
    return valor_de_retorno

# Definición de la función
def saludar(nombre):
    return f"Hola, {nombre}!"

# Llamada a la función
print(saludar("Juan"))  # Output: Hola, Juan!

# Función sin parámetros ni valor de retorno
def mostrar_mensaje():
    print("Este es un mensaje.")

mostrar_mensaje()  # Output: Este es un mensaje.


"""

# Ejemplo Parámetros
print("### Ejemplo Parámetros ###")

nombre = input(str("Introduce tu nombre: "))

def mostrarTuNombre():
    print(f"Tu nombre es: {nombre}")

mostrarTuNombre()

# Ejemplo con funciones y parámetros (tabla de multiplicar con funciones)

print("### Ejemplo con funciones y parámetros (tabla de multiplicar con funciones) ###")

numero = int(input("Introduce un número para ver su tabla de multiplicar: "))

def tablaMultiplicar():
    print(f"Tabla de multiplicar del {numero}:")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")
    return "Tabla generada correctamente."

print(tablaMultiplicar())

# Ejemplo parametros opcionales
print("### Ejemplo parametros opcionales ###")

# Parametros Opcionales
def getEmpleado(nombre, dni = None):
    print("\n")
    print("Empleado:")
    print(f"Nombre: {nombre}")
    
    if dni != None:
        print(f"DNI: {dni}")
    print("\n")

getEmpleado("Juan", "12345678A")
getEmpleado("Ana")


# Ejemplo poarametros opcionales y return
print("### Ejemplo return ###")

num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))

def calculadora(num1, num2):
    suma = num1 + num2
    resta = num1 - num2
    multiplicacion = num1 * num2
    division = num1 / num2

    return print(f"El valor de la suma es {suma}, el valor de la resta es {resta},\nel valor de la multiplicacion es {multiplicacion} y el valor de la division es {division}\n")

calculadora(num1, num2)

# Ejemplo Funciones dentro de otras funciones
print("### Ejemplo Funciones dentro de otras funciones ###")

def getNombre(nombre):
    texto = f"El nombre es: {nombre}"
    return texto
def getApellido(apellido):
    texto = f"El apellido es: {apellido}"
    return texto

def devuelveTodo(nombre, apellido):
    texto = getNombre(nombre) + "\n" + getApellido(apellido)
    return texto

print(devuelveTodo("Juan", "Pérez"))
print(devuelveTodo("Ana", "García"))

# Ejemplo Funciones Lambda
"""
Es una función anónima, es decir, una función que no está ligada a un nombre.
Se utiliza para crear funciones pequeñas y de una sola línea de código.
"""
print("### Ejemplo Funciones Lambda ###")

dime_el_year = lambda year: f"El año es {year * 50}"

print(dime_el_year(2024))
# Nos devolverá el año que pasemos multiplicado por 50
print(dime_el_year(1))

