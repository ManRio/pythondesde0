#Capturar excepciones y manejar errores en codigo Susceptible a fallos/errores

"""
nombre = input("¿Cuál es tu nombre?: ")

try:
    if len(nombre) >= 1:
        nombre_usuario = "El nombre es: " + nombre

    print(nombre_usuario)
except:
    print("Ha ocurrido un error, introduzca bien su nombre por favor.")
else:
    print("Todo ha funcionado correctamente")
finally:
    print("¡FIN DE LA ITERACIÓN!")

"""

# Multiples excepciones
"""
try: 
    numero = int(input("Número para elevarlo al cuadrado: "))
    print("El cuadrado es: "+str(numero*numero))
except TypeError:
    print("Debes convertir tus cadenas a enteros!!")
except ValueError:
    print("Introduce un numero correcto")
except Exception as e:
    print(type(e))
    print("Ha ocurrido un error: ", type(e).__name__)

"""
# Excepciones personalizadas

nombre = input("introduce el nombre: ")
edad = int(input("Introduce la edad: "))

try:
    if edad < 5 or edad > 110:
        raise ValueError("La edad introducida no es real")
    elif len(nombre) <= 1:
        raise ValueError("El nombre no está completo")
    else:
        print(f"Bienvenido {nombre}, pasa y disfruta!!")
except ValueError:
    print("Introduce los datos correctamente")
except Exception as e:
    print("Existe un error: ", e)
