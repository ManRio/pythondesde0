"""
DICCIONARIO:

Un tipo de dato que almacena un conjunto de datos.
En un formato clave > valor.
Es parecido a un array asociativo o un objeto json.

"""
persona = {
    "nombre": "Manuel",
    "apellidos": "Ríos",
    "web": "manrio.dev"
}

print(persona)
print(persona["web"])

# Listas con diccionarios

contactos =  [
    {
        "nombre": "Antonio",
        "mail": "antonio@antonio.com"
    },
    {
        "nombre": "Luis",
        "mail": "luis@luis.com"
    },
    {
        "nombre": "Salvador",
        "mail": "salvador@salvador.com"
    }
]

print(contactos[0]["nombre"])

print("\nListado de contactos")
print("-------------------------------------------")
for contacto in contactos:
    print(f"Nombre del contacto: {contacto["nombre"]}")
    print(f"Email del contacto: {contacto["mail"]}")
    print("-------------------------------------------")
print("*****FIN DE LA AGENDA*****")