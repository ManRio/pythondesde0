"""
EJERCICIO:
Crea una calculadora que tenga dos entradas de texto.
4 botones para las 4 operaciones básicas (suma, resta, multiplicación y división)
y muestre el resultado en una alerta.

"""
from tkinter import *
from tkinter import messagebox as Messagebox

class Calculadora:

    def __init__(self, messagebox):
        self.numero1 = StringVar()
        self.numero2 = StringVar()
        self.resultado = StringVar()
        self.messagebox = messagebox

    def cFloat(self, numero):
        try:
            result = float(numero)
        except:
            result = 0
            Messagebox.showerror("Error", "Debe ingresar un número válido")
        return result


    def sumar(self):
        self.resultado.set(self.cFloat(self.numero1.get()) + self.cFloat(self.numero2.get()))
        self.mostrarResultado()


    def restar(self):
        self.resultado.set(self.cFloat(self.numero1.get()) - self.cFloat(self.numero2.get()))
        self.mostrarResultado()


    def multiplicar(self):
        self.resultado.set(self.cFloat(self.numero1.get()) * self.cFloat(self.numero2.get()))
        self.mostrarResultado()



    def dividir(self):
        if self.numero2.get() == "0":
            Messagebox.showerror("Error", "No se puede dividir entre 0")
            return
        self.resultado.set(self.cFloat(self.numero1.get()) / self.cFloat(self.numero2.get()))
        self.mostrarResultado()

    def mostrarResultado(self):
        Messagebox.showinfo("Resultado", f"El resultado es: {self.resultado.get()}")
        self.numero1.set("")
        self.numero2.set("")


# Creamos y configuramos la ventana
ventana = Tk()
ventana.title("Ejercicio Completo con Tkinter")
ventana.config(bd=25)


marco=Frame(ventana, width=340, height=200)
marco.config(
    padx=15,
    pady=15,
    bd=5,
    relief=SOLID
    )
marco.pack(side=TOP, anchor=CENTER)
marco.pack_propagate(False)

# Instanciar la calculadora
calc = Calculadora(Messagebox)

Label(marco, text="Primer número: ").pack()
Entry(marco, textvariable=calc.numero1, justify="center").pack()

Label(marco, text="Segundo número: ").pack()
Entry(marco, textvariable=calc.numero2, justify="center").pack()

Label(marco, text="").pack()

Button(marco, text="Sumar", command=calc.sumar).pack(side=LEFT, fill=X, expand=True)
Button(marco, text="Restar", command=calc.restar).pack(side=LEFT, fill=X, expand=True)
Button(marco, text="Multiplicar", command=calc.multiplicar).pack(side=LEFT, fill=X, expand=True)
Button(marco, text="Dividir", command=calc.dividir).pack(side=LEFT, fill=X, expand=True)



ventana.mainloop()