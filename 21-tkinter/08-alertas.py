from tkinter import *
from tkinter import messagebox as Messagebox

ventana = Tk()
ventana.title("Alertas")
ventana.geometry("300x200")


def sacarAlerta():
    Messagebox.showinfo("Alerta", "Esto es una alerta")

def sacarWarning():
    Messagebox.showwarning("Alerta", "Esto es un Warning")

def sacarError():
    Messagebox.showerror("Alerta", "Esto es un Error")

def sacarPregunta(nombre):
    resultado = Messagebox.askquestion("Pregunta", "¿Quieres salir de la aplicación?")
    if resultado == "yes":
        Messagebox.showinfo("Adiós", f"Gracias por usar la aplicación {nombre}")
        ventana.destroy()

Button(ventana, text="Mostrar Alerta!!", command=sacarAlerta).pack(anchor=CENTER, expand=True)
Button(ventana, text="Mostrar Warning!!", command=sacarWarning).pack(anchor=CENTER, expand=True)
Button(ventana, text="Mostrar Error!!", command=sacarError).pack(anchor=CENTER, expand=True)

Button(ventana, text="Cerrar Programa", command=lambda: sacarPregunta("Manuel")).pack(anchor=CENTER, expand=True)

ventana.mainloop()