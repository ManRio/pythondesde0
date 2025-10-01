cantantes = ["2Pac", "Drake", "BadBunny", "Julio Iglesias"]

numeros = [1, 2, 5, 8, 3, 4]


# Ordenar lista
print(numeros)
numeros.sort() #Ordena de menor a mayor
print(numeros)

# Añadir Elementos
cantantes.append("lola indigo")
cantantes.insert(1, "Bisbal")

print(cantantes)

#eliminar elementos
cantantes.pop(1)
print(cantantes)

cantantes.remove("BadBunny")
print(cantantes)

# Dar la vuelta

numeros.reverse()
print(numeros)

#Buscar dentro de una lista

print("Drake" in cantantes) # Devuelve true si lo encuentra

#Contar elementos
print(len(cantantes)) # indica cuantos elementos hay en la lista

#Cuantas veces aparece un elemento
numeros.append(8)
print(numeros.count(8))

# Conseguir indice
print(cantantes.index("Drake"))

# Unir Listas
cantantes.extend(numeros)
print(cantantes)
