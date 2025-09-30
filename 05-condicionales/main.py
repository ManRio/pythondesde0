"""
# Condicional IF

Si se_cumple_esta_condición:
    Ejecutar grupo_de_instrucciones
Si_no:
    Ejecutar_otro_grupo_de_instrucciones

if condicion:
    instrucciones
else:
    otras_instrucciones

# Operadores de comparación
Igual: ==
!= Diferente
< Menor que
> Mayor que
<= Menor o igual que
>= Mayor o igual que

# Operadores lógicos
and Y
or O
not Negación

# Operadores de identidad
is Es el mismo objeto
is not No es el mismo objeto

# Operadores de pertenencia
in Está en
not in No está en

"""

# Ejemplo 1

print("########## EJEMPLO 1 ##########")

#color = "rojo"

color = input("Adivina mi color favorito: ")
if color == "rojo":
    print("¡Has acertado!")
    print("El color es rojo")
else:
    print("Color Incorrecto")

# Ejemplo 2
print("########## EJEMPLO 2 ##########")

year = int(input("¿En qué año estamos? "))

if year >= 2024:
    print("Estamos en 2024 o en un año posterior")
else:
    print("Estamos en un año anterior a 2024")

# Ejemplo 3 (if anidados)
print("########## EJEMPLO 3 ##########")

nombre = input("¿Cómo te llamas? ")
ciudad = input("¿En qué ciudad vives? ")
continente = input("¿En qué continente vives? ")
edad = int(input("¿Cuántos años tienes? "))
mayoria_edad = 18

if edad >= mayoria_edad:
    print(f"{nombre} es mayor de edad")

    if continente.lower() == "europa":
        print (f"El/la usuari@ {nombre} es Europe@ y vive en la ciudad de {ciudad}")
    else:
        print(f"El/la usuari@ {nombre} no es Europe@")
else:
    print(f"{nombre} No es mayor de edad")

# Ejemplo 4 (if, elif, else)
print("########## EJEMPLO 4 ##########")

dia = int(input("Dime un día de la semana (1-7): "))

if dia == 1:
    print("Es Lunes")
else:
    if dia == 2:
        print("Es Martes")
    else:
        if dia == 3:
            print("Es Miércoles")
        else:
            if dia == 4:
                print("Es Jueves")
            else:
                if dia == 5:
                    print("Es Viernes")
                else:
                    if dia == 6:
                        print("Es Sábado")
                    else:
                        if dia == 7:
                            print("Es Domingo")
                        else:
                            print("El número no es correcto")

# versión con elif (else if)
print("########## EJEMPLO 4 (versión con elif) ##########")
dia = int(input("Dime un día de la semana (1-7): "))

if dia == 1:
    print("Es Lunes")
elif dia == 2:
    print("Es Martes")
elif dia == 3:
    print("Es Miércoles")
elif dia == 4:
    print("Es Jueves")
elif dia == 5:
    print("Es Viernes")
elif dia == 6:
    print("Es Sábado")
elif dia == 7:
    print("Es Domingo")
else:
    print("El número no es correcto")

# Ejemplo 5 (operadores lógicos y multiples condiciones)
print("########## EJEMPLO 5 ##########")

edad_minima = 18
edad_maxima = 65
edad_oficial = int(input("¿Cuántos años tienes? "))

if edad_oficial >= edad_minima and edad_oficial <= edad_maxima:
    print("Puedes trabajar")
else:
    print("No puedes trabajar")

# Ejemplo 6 (operadores lógicos y múltiples condiciones)
print("########## EJEMPLO 6 ##########")

pais = input("¿De qué país eres? ")
if pais.lower() == "mexico" or pais.lower() == "españa" or pais.lower() == "colombia":
    print(f"Puedes entrar al club, {pais} es un país de habla hispana")
else:
    print(f"No puedes entrar al club, {pais} no es un país de habla hispana")

# Si se cumple una de las tres condiciones anteriores, se permite la entrada al club, en caso de que no se cumpla ninguna, se deniega la entrada.

# Ejemplo 7 (operador logico de negacion not)

print("########## EJEMPLO 7 ##########")
pais = input("¿De qué país eres? ")
if not (pais.lower() == "mexico" or pais.lower() == "españa" or pais.lower() == "colombia"):
    print(f"No puedes entrar al club, {pais} no es un país de habla hispana")
else:
    print(f"Puedes entrar al club, {pais} es un país de habla hispana")

# Ejemplo 8 (operador de comparación !=)
print("########## EJEMPLO 8 ##########")
pais = input("¿De qué país eres? ")

if pais.lower() != "mexico" and pais.lower() != "españa" and pais.lower() != "colombia":
    print(f"No puedes entrar al club, {pais} no es un país de habla hispana")
else:
    print(f"Puedes entrar al club, {pais} es un país de habla hispana")





