from tkinter import *

ventana = Tk()
ventana.title("Menus en Tkinter")

mi_menu = Menu(ventana)
ventana.config(menu=mi_menu, width=300, height=300)

archivo = Menu(mi_menu, tearoff=0)
archivo.add_command(label="Nuevo")
archivo.add_command(label="Nueva ventana")
archivo.add_separator()
archivo.add_command(label="Abrir Archivo")
archivo.add_command(label="Abrir Carpeta")
archivo.add_separator()
archivo.add_command(label="Salir", command=ventana.quit)

mi_menu.add_cascade(label="Archivo", menu=archivo)
mi_menu.add_command(label="Editar")
mi_menu.add_command(label="Seleccion")
mi_menu.add_separator()
mi_menu.add_command(label="Cerrar", command=ventana.quit)




ventana.mainloop()