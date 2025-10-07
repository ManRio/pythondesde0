import notas.nota as modelo

class Acciones:

    def crear(self, usuario):
        print(f"\nOK {usuario[1]} vamos a crear una nueva nota...")

        titulo = input("Introduce el título de la nota: ")
        descripcion = input("Introduce el contenido de la nota: ")

        nota = modelo.Nota(usuario[0], titulo, descripcion)
        guardar = nota.guardar()
        if guardar[0] >= 1:
            print(f"\nPerfecto {usuario[1]} has creado la nota: {guardar[1].titulo}")
        else:
            print("\nLa nota no se ha guardado correctamente")

    def mostrar(self, usuario):

        print(f"\nVale {usuario[1]} aquí tienes tus notas:")

        nota = modelo.Nota(usuario[0], '', '')
        notas = nota.listar()

        if len(notas) >= 1:
            for n in notas:
                print("\n----------------")
                print(n[2])
                print(n[3])
                print("Creada el día: " + str(n[4]))
                print("----------------")
        else:
            print("\nNo tienes notas creadas aún")

    def borrar (self, usuario):
        print(f"\n Ok {usuario[1]} vamos a eliminar una nota")
        titulo = input("Introduce el título de la nota a eliminar: ")
        nota = modelo.Nota(usuario[0], titulo, '')
        eliminar = nota.eliminar(titulo)
        if eliminar[0] >= 1:
            print(f"\nPerfecto {usuario[1]} has eliminado la nota titulada: {titulo}")
        else:
            print("\nNo se ha encontrado ninguna nota con ese título")



