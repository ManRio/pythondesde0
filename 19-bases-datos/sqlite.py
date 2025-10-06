# Importar modulo
import sqlite3

# conexion

conexion = sqlite3.connect('pruebas.db')

# crear cursor
cursor = conexion.cursor()

# Crear tabla
"""
cursor.execute("CREATE TABLE IF NOT EXISTS productos("+
"id INTEGER PRIMARY KEY AUTOINCREMENT,"+
"titulo VARCHAR(255), "+
"descripcion TEXT, "+
"precio int(255)"
")")

# Confirmar cambios (importante para CREATE/INSERT/UPDATE/DELETE)
conexion.commit()

# Insertar datos
cursor.execute("INSERT INTO productos VALUES (null, 'Primer Producto', 'descripcion de mi producto', 550)")
conexion.commit()

# Listar datos
cursor.execute("SELECT * FROM productos")
productos = cursor.fetchall()

for producto in productos:
    print("\n--------------------------")
    print("Titulo: "+producto[1])
    print("Descripción: "+producto[2])
    print("Precio: "+str(producto[3]))
    print("\n--------------------------")

cursor.execute("SELECT titulo FROM productos")
producto = cursor.fetchone()
print(producto)

# Eliminar datos o registros
cursor.execute("DELETE FROM productos")
conexion.commit()
"""

#Insertar muchos registros de golpe
productos = [
    ("Ordenador portatil", "Buen PC", 700),
    ("Telefono Movil", "Buen teléfono", 140),
    ("Placa base", "Buena Placa", 80),
    ("Tablet 15'", "Buena tablet", 300)
]
cursor.executemany("INSERT INTO productos VALUES (null, ?, ?, ? )", productos)
conexion.commit()

# Listar datos
cursor.execute("SELECT * FROM productos")
productos = cursor.fetchall()

for producto in productos:
    print("\n--------------------------")
    print("ID: "+str(producto[0]))
    print("Titulo: "+producto[1])
    print("Descripción: "+producto[2])
    print("Precio: "+str(producto[3]))
    print("\n--------------------------")

cursor.execute("SELECT titulo FROM productos")
producto = cursor.fetchone()
print(producto)

#cerrar conexion
conexion.close()

