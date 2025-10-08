from tkinter import *

ventana = Tk()
#ventana.geometry("800x600")

texto = Label(ventana, text="Bienvenido a mi programa")

texto.config(
    fg="white",
    bg="#000000",
    padx=50,
    pady=20,
    font=("Consolas", 30, "bold italic")
)
texto.pack(side=TOP, anchor="center") # Con side podemos indicar la posicion relativa al padre (ventana) y con anchor la posicion absoluta en la ventana

texto = Label(ventana, text="Soy Manuel Ríos")

texto.config(
    justify="right",
    height=3,
    fg="blue",
    bg="grey",
    font=("Arial", 18, "bold"),
    padx=20,
    pady=10,
    cursor="pirate",
)
texto.pack(side=TOP, expand=YES, fill=X) # Con expand hacemos que el widget crezca para ocupar todo el espacio disponible en la direccion del side, y con fill indicamos que rellene en la direccion indicada (X o Y)

texto = Label(ventana, text="Basico")
texto.config(
    justify="right",
    height=3,
    fg="black",
    bg="green",
    font=("Arial", 18, "bold"),
    padx=20,
    pady=10,
    cursor="tcross",
)
texto.pack(side=LEFT, fill=X, expand=YES)

texto = Label(ventana, text="Pruebas en Tkinter")

texto.config(
    justify="right",
    height=3,
    fg="white",
    bg="red",
    font=("Arial", 18, "bold"),
    padx=20,
    pady=10,
    cursor="dotbox",
)
texto.pack(side=LEFT, fill=X, expand=YES)

texto = Label(ventana, text="Pruebas en Tkinter")

texto.config(
    justify="right",
    height=3,
    fg="black",
    bg="orange",
    font=("Arial", 18, "bold"),
    padx=20,
    pady=10,
    cursor="spraycan",
)
texto.pack(side=LEFT, fill=X, expand=YES)


ventana.mainloop()