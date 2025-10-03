from coche import Coche

carro = Coche("Amarillo", "Renault", "Clio", 150, 200, 4)
carro1 = Coche("Verde", "Seat", "Panda", 240, 200, 4)
carro2 = Coche("Azul", "Citroen", "Xsara", 100, 180, 5)
carro3 = Coche("Rojo", "Mercedes", "Clase A", 350, 400, 4)

print(carro.getColor())

print(carro.getInfo())
print(carro1.getInfo())
print(carro2.getInfo())
print(carro3.getInfo())

# Detectar el tipado de objetos

carro3 = "Aleatorio"

if type(carro3) == Coche:
    print("es un objeto correcto de tipo Coche !!")
else:
    print("NO ES UN OBJETO CORRETO DE TIPO COCHE !! ")

# Visibilidad

print(carro.soy_publico)
# print(carro.__soy_privado) # No accederá a la propiedad, dará error
print(carro.getPrivado()) #para acceder a una propiedad o atributo privado es necesario un metodo getter