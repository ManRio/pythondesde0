import mysql.connector

def conectar():
    database = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="master_python",
        port=3306
    )
    cursor = database.cursor(buffered=True) # Permite que el cursor pueda recorrer los registros más de una vez

    return [database, cursor]
