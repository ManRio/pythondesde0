from tkinter import *

ventana = Tk()
ventana.geometry("800x600")

texto = Label(ventana, text="Bienvenido a mi programa")

texto.config(
    fg="white",
    bg="#000000",
    padx=50,
    pady=20,
    font=("Consolas", 30, "bold italic")
)
texto.pack()

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
texto.pack(anchor="sw")

def pruebas(nombre, apellidos, pais):
    return f"Hola {nombre} {apellidos}, veo que eres de {pais}"

texto = Label(ventana, text=pruebas(nombre="Manuel", apellidos="Ríos", pais="España")) # Keyword arguments, podemos pasar los argumentos en cualquier orden
texto.config(
    justify="right",
    height=3,
    fg="black",
    bg="green",
    font=("Arial", 18, "bold"),
    padx=20,
    pady=10,
    cursor="pirate",
)
texto.pack(anchor="center")

texto = Label(ventana, text="Pruebas en Tkinter")

texto.config(
    justify="right",
    height=3,
    fg="red",
    bg="grey",
    font=("Arial", 18, "bold"),
    padx=20,
    pady=10,
    cursor="pirate",
)
texto.pack(anchor="ne")


ventana.mainloop()