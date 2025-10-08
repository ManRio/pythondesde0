#Tkinter es un modulo para crear interfaces gráficas de usuario (GUI)
from tkinter import *
import os


class Programa:

    def __init__(self):
        self.title = "Ventana de pruebas"
        self.icon = "icono.ico"
        self.icon_alt = "./21-tkinter/icono.ico"
        self.size = "770x470"
        self.resizable = False

    def cargar(self):
        # Creamos una ventana
        ventana = Tk()
        self.ventana = ventana

        # Título de la ventana
        ventana.title(self.title)

        # Dimensiones de la ventana
        ventana.geometry(self.size)

        # Icono de la ventana
        ventana.iconbitmap(self.icon)

        ruta_icono = os.path.abspath(self.icon)

        if not os.path.isfile(ruta_icono):
            ruta_icono = os.path.abspath(self.icon_alt)

        # Mostrar texto en el programa
        texto = Label(ventana, text="Hola, soy una ventana")
        texto.pack() # pack() es un método que añade el texto a la ventana

        # Evitar que se pueda redimensionar la ventana
        if not self.resizable:
            ventana.resizable(1,1)
        else:
            ventana.resizable(0, 0)  # (ancho, alto) 0 = no, 1 = si

        # Color de fondo de la ventana
        ventana.config(bg="#2c3e50")

    def add_texto(self):
        texto = Label(self.ventana, text="Hola, desde un metodo")
        texto.pack() # pack() es un método que añade el texto a la ventana
    
    def mostrar(self):
        self.ventana.mainloop() # mainloop() es un bucle infinito que mantiene la ventana abierta
        # hasta que el usuario la cierra.


# instanciar mi programa
mi_programa = Programa()
mi_programa.cargar()
mi_programa.add_texto()
mi_programa.mostrar()