from tkinter import *

ventana = Tk()

ventana.title("Formularios 2")
ventana.geometry("800x500")

encabezado = Label(ventana, text="Formularios 2")
encabezado.config(
    padx=15,
    pady=15,
    bg="lightgray",
    fg="blue",
    font=("Consolas", 20)
)
encabezado.grid(row=0, column=0, columnspan=6, sticky=W)

# Botones check
def mostrarProfesion():
    texto = ""
    if Web.get():
        texto += "Desarrollo Web "
    if Movil.get():
        if Web.get():
            texto += "y Desarrollo Movil"
        else:
            texto += "Desarrollo Movil"

    mostrar.config(
        text=texto,
        bg="green",
        fg="white",
        padx=10,
        pady=10,
        font=("Consolas", 15)
    )


Web = IntVar()
Movil = IntVar()

Label(ventana, text="¿A que te dedicas?: ").grid(row=1, column=0)
Checkbutton(
    ventana,
    text="Desarrollo Web",
    variable=Web,
    onvalue=1,
    offvalue=0,
    command= mostrarProfesion
    ).grid(row=2, column=0)
Checkbutton(
    ventana,
    text="Desarrollo Movil",
    variable=Movil,
    onvalue=1,
    offvalue=0,
    command= mostrarProfesion
    ).grid(row=3, column=0)
mostrar = Label(ventana)
mostrar.grid(row=4, column=0)


# Radio Buttons

def marcar():
    marcado.config(text=opcion.get())


opcion = StringVar()
opcion.set(None)


Label(ventana, text="¿Cual es tu genero?: ").grid(row=5, column=0)
Radiobutton(
    ventana,
    text="Masculino",
    value = "Masculino",
    variable = opcion,
    command=marcar,
    ).grid(row=6)
Radiobutton(
    ventana,
    text="Femenino",
    value = "Femenino",
    variable = opcion,
    command=marcar,
    ).grid(row=7)

marcado = Label(ventana)
marcado.grid(row=8)

# Listas desplegables (Option Menu)

def seleccionar():
    seleccionado.config(text=opcion.get())

opcion = StringVar()
opcion.set("España")

Label(ventana, text="Elige un pais: ").grid(row=5, column=1)

select = OptionMenu(ventana, opcion, "España", "Mexico", "Argentina", "Colombia", "Peru", "Chile")
select.grid(row=6, column=1)

Button(ventana, text="Seleccionar", command=seleccionar).grid(row=6, column=2)

seleccionado = Label(ventana)
seleccionado.grid(row=7, column=1)

ventana.mainloop()