# Programacion Orientada a Objetos (POO o OOP)

# Definir una clase (Molde para crear más objetos de ese tipo
# (Coche) con  características similares )

class Coche:

    # Atributos o propiedades (Variables)
    # Caracteristicas del coche
    color = "Rojo"
    marca = "Ferrari"
    modelo = "F50"
    velocidad = 300
    caballaje = 500
    plazas = 2

    # Metodos, acciones que hace el objeto (funciones)

    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color

    def setModelo(self, modelo):
        self.modelo = modelo

    def getModelo(self):
        return self.modelo

    def acelerar(self):
        self.velocidad += 1

    def frenar(self):
        self.velocidad -= 1

    def getVelocidad(self):
        return self.velocidad

# Fin definicion Clase

# Crear objeto / Instanciar la clase
coche = Coche()

coche.setColor("amarillo")
coche.setModelo("F480")

print("COCHE 1: ")

print(coche.marca, coche.getModelo(), coche.getColor())

print("Velocidad actual: ", coche.getVelocidad())
coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.frenar()

print("Velocidad nueva: ", coche.getVelocidad())

print("\n--------------------------------------\n")

# Crear mas objetos

coche2 = Coche()

coche2.setColor("Verde")
coche2.setModelo("F25R")

print("COCHE 2: ")

print(coche2.marca, coche2.getModelo(), coche2.getColor())

