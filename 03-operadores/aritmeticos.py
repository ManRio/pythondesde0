# Operadores Aritméticos
numero1 = 10
numero2 = 3 # el simbolo = es un operador de asignación

# Suma
suma = numero1 + numero2
print("Suma: ", suma)
# Resta
resta = numero1 - numero2
print("Resta: ", resta)
# Multiplicación
multiplicacion = numero1 * numero2
print("Multiplicación: ", multiplicacion)
# División
division = numero1 / numero2
print("División: ", division)
# División entera
division_entera = numero1 // numero2
print("División entera: ", division_entera)
# Módulo
modulo = numero1 % numero2
print("Módulo: ", modulo)
# Potencia
potencia = numero1 ** numero2
print("Potencia: ", potencia)
# Raíz cuadrada
raiz_cuadrada = numero1 ** (1/2)
print("Raíz cuadrada: ", raiz_cuadrada)
# Raíz cúbica
raiz_cubica = numero1 ** (1/3)
print("Raíz cúbica: ", raiz_cubica)
# Raíz n-ésima
n = 4
raiz_nesima = numero1 ** (1/n)
print(f"Raíz {n}-ésima: ", raiz_nesima)

# Operadores de Asignación
edad = 55
print("Edad inicial: ", edad)

edad += 5  # edad = edad + 5
print("Edad después de += 5: ", edad)

edad -= 2  # edad = edad - 2
print("Edad después de -= 2: ", edad)

edad *= 3  # edad = edad * 3
print("Edad después de *= 3: ", edad)

edad /= 4  # edad = edad / 4
print("Edad después de /= 4: ", edad)

edad //= 2  # edad = edad // 2
print("Edad después de //= 2: ", edad)

edad %= 7  # edad = edad % 7
print("Edad después de %= 7: ", edad)

edad **= 2  # edad = edad ** 2
print("Edad después de **= 2: ", edad)

# Operadores de Incremento y Decremento

year = 2024
print("Año inicial: ", year)

year += 1  # Incremento en 1
print("Año después de incrementar en 1: ", year)

year -= 1  # Decremento en 1
print("Año después de decrementar en 1: ", year)

year = year + 5  # Incremento en 5
print("Año después de incrementar en 5: ", year)
year = year - 3  # Decremento en 3
print("Año después de decrementar en 3: ", year)

# No existen los operadores ++ y -- como en otros lenguajes
# year++  # Error de sintaxis
# year--  # Error de sintaxis
# En Python se usan +=1 y -=1 para estos casos
print("Año final: ", year)



