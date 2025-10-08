from tkinter import *
from PIL import Image, ImageTk

ventana = Tk()
ventana.title("imagenes en Tkinter")
ventana.geometry("800x600")

Label(ventana, text="Imagenes en Tkinter").pack(anchor="w")

imagen = Image.open("./21-tkinter/imagenes/lobo-gris.jpg") # traemos la imagen usando PIL y el objeto Image

render = ImageTk.PhotoImage(imagen) # convertimos la imagen a un objeto PhotoImage de Tkinter usando ImageTk

Label(ventana, image=render).pack(anchor="center") # mostramos la imagen en un Label


ventana.mainloop()
