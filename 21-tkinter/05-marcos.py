from tkinter import *

ventana = Tk()
ventana.title("Marcos")
ventana.config(bg="lightblue")

marcoPadre = Frame(ventana, width=680, height=480)
marcoPadre.config(bg="grey", bd=6, relief="sunken")
marcoPadre.pack(side=TOP, anchor=CENTER, padx=10, pady=10, fill=X, expand=YES)
marcoPadre.pack_propagate(False)

texto = Label(marcoPadre, text="Marcos", bg="lightblue", fg="black")
texto.config(font=("Arial", 20))
texto.pack(fill=X, padx=5, pady=5)


marco1 = Frame(marcoPadre, width=300, height=400)
marco1.config(bg="red", bd=6, relief="groove")
marco1.pack(side=RIGHT, anchor=SE, padx=10, pady=10)
marco1.pack_propagate(False)

etiqueta1 = Label(marco1, text="Marcos", bg="black", fg="white")
etiqueta1.pack(fill=X, padx=5, pady=5)
boton1 = Button(marco1, text="Botón 1")
boton1.pack(side=BOTTOM, padx=5, pady=5)
boton2 = Button(marco1, text="Botón 2")
boton2.pack(side=BOTTOM, padx=5, pady=5)
boton3 = Button(marco1, text="Botón 3")
boton3.pack(side=BOTTOM, padx=5, pady=5)
boton4 = Button(marco1, text="Botón 4")
boton4.pack(side=BOTTOM, padx=5, pady=5)
boton5 = Button(marco1, text="Botón 5")
boton5.pack(side=BOTTOM, padx=5, pady=5)

marco2 = Frame(marcoPadre, width=300, height=400)
marco2.config(bg="green", bd=5, relief="raised")
marco2.pack(side=LEFT, anchor=SW, padx=10, pady=10)
marco2.pack_propagate(False)

etiqueta2 = Label(marco2, text="Marcos", bg="black", fg="white")
etiqueta2.pack(fill=X, padx=5, pady=5)
boton6 = Button(marco2, text="Botón 6")
boton6.pack(side=BOTTOM, padx=5, pady=5)
boton7 = Button(marco2, text="Botón 7")
boton7.pack(side=BOTTOM, padx=5, pady=5)

ventana.mainloop()