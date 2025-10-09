"""
Crear un programa que tenga:
- Una ventana con un título y un tamaño específico. (hecho)
- No redimensionable. (hecho)
- Un menu (Inicio, Añadir, Información, Salir). (hecho)
- Diferentes pantallas que se puedan cambiar desde el menú. (hecho)
- Formulario de añadir productos. (hecho)
- Guardar datos temporalmente (hecho)
- Mostrar los datos listados en la pantalla home.(hecho)
- Opcion de Salir (hecho)
"""

from tkinter import *
from tkinter import ttk

ventana = Tk()
# Primer paso: Crear la ventana
#ventana.geometry("450x500")
ventana.minsize(450, 500)
ventana.title("Proyecto Tkinter")

# Segundo paso: No redimensionable
ventana.resizable(0, 0)

# Cuarto paso: Diferentes pantallas

def home():
    #Montar pantalla de inicio
    home_label.config(
        fg="white",
        bg="black",
        font=("Arial", 30),
        padx=190,
        pady=10
    )
    home_label.grid(row=0, column=0)

    products_box.grid(row=2)
    # Listar productos
    """
    for product in products:
        if len(product) == 3:
            product.append("added")
            Label(products_box, text=product[0]).grid()
            Label(products_box, text=product[1]).grid()
            Label(products_box, text=product[2]).grid()
            Label(products_box, text="------------------").grid()
    """
    for product in products:
        if len(product) == 3:
            product.append("added")
            products_box.insert("", 0, text=product[0], values=(product[1], product[2]))

    # Ocultar los demas labels
    add_label.grid_remove()
    add_frame.grid_remove()
    info_label.grid_remove()
    data_label.grid_remove()
    return True

def add():
    # Encabezado
    add_label.config(
        fg="white",
        bg="black",
        font=("Arial", 30),
        padx=90,
        pady=10
    )
    add_label.grid(row=0, column=0, columnspan=10)
    # Campos del formulario
    add_frame.grid(row=1)
    add_name_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
    add_name_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")
    add_price_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")
    add_price_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")
    add_descripion_label.grid(row=3, column=0, padx=5, pady=5, sticky="ne")
    add_descripion_entry.grid(row=3, column=1, padx=5, pady=5, sticky="w")
    add_descripion_entry.config(
        width=30,
        height=5,
        font=("Consolas", 12),
        padx=5,
        pady=5)
    add_button.grid(row=5, column=1, padx=5, pady=5, sticky="e")
    add_button.config(
        padx=15,
        pady=5,
        bg="green",
        fg="white",
    )
    add_separator.grid(row=4, column=1)

    # Ocultar los demas labels
    home_label.grid_remove()
    info_label.grid_remove()
    data_label.grid_remove()
    products_box.grid_remove()
    return True

def info():
    info_label.config(
        fg="white",
        bg="black",
        font=("Arial", 30),
        padx=120,
        pady=10
    )
    info_label.grid(row=0, column=0)

    data_label.config(
        fg="black",
        bg="white",
        font=("Arial", 15),
        padx=10,
        pady=10
    )
    data_label.grid(row=1, column=0)
    # Ocultar los demas labels
    home_label.grid_remove()
    add_label.grid_remove()
    add_frame.grid_remove()
    products_box.grid_remove()
    return True

# sexto paso: Guardar datos temporalmente
def add_product():
    products.append([
        name_data.get(),
        price_data.get(),
        add_descripion_entry.get("1.0", "end-1c") # Texto multilinea. Parametros (inicio, fin)
    ])
    name_data.set("")
    price_data.set("")
    add_descripion_entry.delete("1.0", END)

    home()

# Quinto paso: Formulario de añadir productos
# Variables Importantes
products = []
name_data = StringVar()
price_data = StringVar()


# Definir campos de pantallas (Inicio)
home_label = Label(ventana, text="Inicio")
#products_box = Frame(ventana, width=250)
Label(ventana).grid(row=1)
products_box = ttk.Treeview(height=12, columns=3)
products_box.grid(row=1, column=0, columnspan=2)
products_box.heading("#0", text="Nombre", anchor=W)
products_box.heading("#1", text="Precio", anchor=W)



# Definir campos de pantallas (Añadir)
add_label = Label(ventana, text="Añadir Producto")
# Campos del formulario
add_frame = Frame(ventana)
add_name_label = Label(add_frame, text="Nombre del producto:")
add_name_entry = Entry(add_frame, textvariable=name_data)
add_price_label = Label(add_frame, text="Precio del producto:")
add_price_entry = Entry(add_frame, textvariable=price_data)
add_descripion_label = Label(add_frame, text="Descripción del producto:")
add_descripion_entry = Text(add_frame)
add_button = Button(add_frame, text="Guardar", command=add_product)
add_separator = Label(add_frame)

# Definir campos de pantallas (Informacion)

info_label = Label(ventana, text="Información")
data_label = Label(ventana, text="Creado por: Manuel Rios - 2025")


# Cargar pantalla de inicio
home()

# Tercer paso: Crear el menú y Octavo paso: Opcion de Salir
menu_superior = Menu(ventana)
menu_superior.add_command(label="Inicio", command=home)
menu_superior.add_command(label="Añadir", command=add)
menu_superior.add_command(label="Información", command=info)
menu_superior.add_command(label="Salir", command=ventana.quit)

# Asignar el menu a la ventana
ventana.config(menu=menu_superior)


ventana.mainloop()