"""
EJERCICIO 5.
Crear una lista con el contenido de esta tabla
ACCION      AVENTURA                DEPORTES
GTA         ASSASINS                FIFA 25
COD         CRASH BANDICOOT         PRO 25
PUGB        PRINCE OF PERSIA        MOTOGP 25

Mostrar esta información ordenada
"""

tabla = [
    {
        "categoria" : "Accion",
        "juegos" : ["GTA", "COD", "PUGB"]
    },
    {
        "categoria" : "Aventura",
        "juegos" : ["Assasins", "Crash Bandicoot", "Prince Of Persia"]
    },
    {
        "categoria" : "Deportes",
        "juegos" : ["Fifa 25" , "Pro 25", "MotoGP 25"]
    },
]


# Hecho con bucle while
print("------- Con Bucle While -------")
for categoria in tabla:
    print(f"\nDe la categoría {categoria['categoria']} tenemos los siguientes juegos: ")

    contador = 0
    while contador < len(categoria['juegos']):
        print(f"{contador+1} - {categoria['juegos'][contador]}")
        contador += 1

# Hecho con doble for (mas sencillo)
print("------- Con doble for -------")
for categoria in tabla:
    print(f"--------------{categoria['categoria']}--------------")
    for juego in categoria['juegos']:
        print(juego)

print("### Fin del Script ###")

