"""
EJERCICIO:
Crea una calculadora que tenga dos entradas de texto.
4 botones para las 4 operaciones básicas (suma, resta, multiplicación y división)
y muestre el resultado en una alerta.

"""
from tkinter import *
from tkinter import messagebox as Messagebox

# Creamos y configuramos la ventana
ventana = Tk()
ventana.title("Ejercicio Completo con Tkinter")
ventana.config(bd=25)

#funciones
def cFloat(numero):
    try:
        result = float(numero)
    except:
        result = 0
        Messagebox.showerror("Error", "Debe ingresar un número válido")
    return result


def sumar():
    resultado.set(cFloat(numero1.get()) + cFloat(numero2.get()))
    mostrarResultado()


def restar():
    resultado.set(cFloat(numero1.get()) - cFloat(numero2.get()))
    mostrarResultado()


def multiplicar():
    resultado.set(cFloat(numero1.get()) * cFloat(numero2.get()))
    mostrarResultado()



def dividir():
    if numero2.get() == "0":
        Messagebox.showerror("Error", "No se puede dividir entre 0")
        return
    resultado.set(cFloat(numero1.get()) / cFloat(numero2.get()))
    mostrarResultado()

def mostrarResultado():
    Messagebox.showinfo("Resultado", f"El resultado es: {resultado.get()}")
    numero1.set("")
    numero2.set("")



numero1 = StringVar()
numero2 = StringVar()
resultado = StringVar()

marco=Frame(ventana, width=340, height=200)
marco.config(
    padx=15,
    pady=15,
    bd=5,
    relief=SOLID
    )
marco.pack(side=TOP, anchor=CENTER)
marco.pack_propagate(False)

Label(marco, text="Primer número: ").pack()
Entry(marco, textvariable=numero1, justify="center").pack()

Label(marco, text="Segundo número: ").pack()
Entry(marco, textvariable=numero2, justify="center").pack()

Label(marco, text="").pack()

Button(marco, text="Sumar", command=sumar).pack(side=LEFT, fill=X, expand=True)
Button(marco, text="Restar", command=restar).pack(side=LEFT, fill=X, expand=True)
Button(marco, text="Multiplicar", command=multiplicar).pack(side=LEFT, fill=X, expand=True)
Button(marco, text="Dividir", command=dividir).pack(side=LEFT, fill=X, expand=True)



ventana.mainloop()