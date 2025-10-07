import usuarios.conexion as conexion

connect = conexion.conectar()
database = connect[0]
cursor = connect[1]


class Nota:
    def __init__(self, usuario_id, titulo, descripcion):
        self.usuario_id = usuario_id
        self.titulo = titulo
        self.descripcion = descripcion

    def guardar(self):
        sql = "INSERT INTO notas VALUES (null, %s, %s, %s, NOW())"
        nota = (self.usuario_id, self.titulo, self.descripcion)

        try:
            cursor.execute(sql, nota)
            database.commit()
            return [cursor.rowcount, self]  # rowcount devuelve el número de registros afectados y self devuelve el objeto creado
        except Exception as e:
            print(f"Error: {e}")
            return [0, self]

    def listar(self):
        sql = f" SELECT * FROM notas WHERE usuario_id = {self.usuario_id} ORDER BY id DESC"

        cursor.execute(sql)
        result = cursor.fetchall()

        return result
    
    def eliminar(self, titulo):
        sql = f"DELETE FROM notas WHERE usuario_id = {self.usuario_id} AND titulo LIKE '%{titulo}%'"
        cursor.execute(sql)

        database.commit()
        return [cursor.rowcount, self]
        # rowcount devuelve el número de registros afectados y self devuelve el objeto creado
        # Si rowcount es 0, no se ha eliminado ninguna nota
        # Si rowcount es 1, se ha eliminado una nota