import mysql.connector

#conexión a la base de datos
database = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="master_python"
)

#¿la conexion ha sido correcta?
#print(database)

# Cursor - Permite ejecutar sentencias de sql
cursor = database.cursor()

#crear base de datos
cursor.execute("CREATE DATABASE IF NOT EXISTS master_python")
cursor.execute("SHOW DATABASES")
cursor.fetchall()

"""
for bd in cursor:
    print(bd)

"""

    #Crear tablas
cursor.execute("""
CREATE TABLE IF NOT EXISTS vehiculos(
    id int(10) auto_increment not null,
    marca varchar(40) not null,
    modelo varchar(40) not null,
    precio float(10,2) not null,
    CONSTRAINT pk_vehiculo PRIMARY KEY(id)
)
""")

"""
cursor.execute("SHOW TABLES")

for table in cursor:
    print(table)

"""

#cursor.execute("INSERT INTO vehiculos VALUES (null, 'Opel', 'Astra', 18500)")

coches = [
    ('Seat', 'Ibiza', 5000),
    ('Renault', 'Clio', 12000),
    ('Citroen', 'Saxo', 13000),
    ('Mercedes', 'Clase C', 35000)
]

#cursor.executemany("INSERT INTO vehiculos VALUES (null, %s, %s, %s)", coches)

database.commit()

cursor.execute("SELECT * FROM vehiculos WHERE precio >= 10000 ORDER BY precio DESC")

result = cursor.fetchall()

print("----- Coches mayores a 10000€ -----")
for coche in result:
    print(coche)

cursor.execute("SELECT * FROM vehiculos")

result = cursor.fetchall()

print("\n----- Todos mis coches -----")
for coche in result:
    print(coche)

# Borrar y Actualizar registros
cursor.execute("DELETE FROM vehiculos WHERE marca = 'Renault'")
database.commit()
cursor.execute("UPDATE vehiculos SET precio = 45000 WHERE marca = 'Mercedes'")
database.commit()
cursor.execute("SELECT * FROM vehiculos")
result = cursor.fetchall()
print("\n----- Actualizar y Borrar -----")
for coche in result:
    print(coche)

#cerrar conexion
cursor.close()
database.close()
