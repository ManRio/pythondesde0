"""
Proyecto Python y MySQL:
Este proyecto es una aplicación de consola en Python que interactúa con una base de datos MySQL.
- Abrir Asistente
- Login o Registro
- Si elegimos Registro, creara un usuario en la base de datos
- Si elegimos Login, validara el usuario y contraseña con la base de datos y nos preguntará:
    - Crear Nota
    - Mostrar Notas
    - Eliminar Nota
    - Salir
"""
from usuarios import acciones

print("""
ACCIONES DISPONIBLES:
    - Registro
    - Login
""")
hazEl = acciones.Acciones()

accion = input("¿Qué quieres hacer?: ")

if accion == "Registro" or accion == "registro":
    hazEl.registro()

elif accion == "Login" or accion == "login":
    hazEl.login()