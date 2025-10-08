from tkinter import *

ventana = Tk()
ventana.geometry("700x400")
ventana.title("Formularios en Tkinter")

# Texto Encabezado
encabezado = Label(ventana, text="Formularios en Tkinter")
encabezado.config(
    fg="white",
    bg="darkblue",
    padx=20,
    pady=10,
    font=("Open Sans", 18, "bold"),
    relief=FLAT
)
encabezado.grid(row=0, column=0, columnspan=12, sticky=NW)

#Label para el campo de texto(nombre)
label = Label(ventana, text="Nombre: ")
label.grid(row=1, column=0, padx=5, pady=5)

# Campo de Texto(nombre)
campo_texto = Entry(ventana)
campo_texto.grid(row=1, column=1, sticky=W, padx=5, pady=5)

#Label para el campo de texto(apellido)
label = Label(ventana, text="Apellidos: ")
label.grid(row=2, column=0, padx=5, pady=5)

# Campo de Texto(apellido)
campo_texto = Entry(ventana)
campo_texto.grid(row=2, column=1, sticky=W, padx=5, pady=5)
campo_texto.config(justify="left", state="normal")

#Label para el campo de texto(descripcion)
label = Label(ventana, text="Descripcion: ")
label.grid(row=3, column=0, sticky=N, padx=5, pady=5)

# Campo de Texto(descripcion)
campo_grande = Text(ventana)
campo_grande.grid(row=3, column=1, padx=5, pady=5)
campo_grande.config(
    width=30,
    height=5,
    font=("Consolas", 12),
    padx=15,
    pady=15,
    )
campo_grande.insert(1.0, "Descripcion del usuario...")

# Boton
Label(ventana).grid(row=4, column=1)

boton = Button(ventana, text="Enviar")
boton.grid(row=5, column=1, sticky=W, padx=5, pady=5)
boton.config(
    padx=10,
    pady=5,
    bg="darkblue",
    fg="white",
    font=("Open Sans", 12, "bold"),
    activebackground="blue",
    activeforeground="red",
    cursor="hand2",
    relief=FLAT
)

ventana.mainloop()
