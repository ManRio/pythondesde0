from flask import Flask, redirect, url_for, render_template
from datetime import datetime

app = Flask(__name__)

# Context processors

@app.context_processor
def date_now():
    return {
        'now': datetime.utcnow()
    }

# Endpoints
@app.route('/')
def index():

    edad = 19
    personas = ["Manuel", "Aurelio", "Juan", "Ana", "Maria"]

    return render_template(
                "index.html",
                edad=edad,
                personas=personas,
                dato1="valor",
                dato2="otro valor",
                lista=["uno", "dos", "tres", "cuatro"]
                )

@app.route('/informacion')
@app.route('/informacion/<nombre>')
def informacion(nombre = None):

    texto = "Desconocido"
    if nombre != None:
        texto = f"Bienvenido {nombre}"

    return render_template("informacion.html", texto=texto)

@app.route('/contacto')
@app.route('/contacto/<redireccion>')
def contacto(redireccion = None):
    
    if redireccion != None:
        return redirect(url_for("lenguajes"))

    return render_template("contacto.html")

@app.route('/lenguajes-de-programacion')
def lenguajes():
    return render_template("lenguajes.html")

if __name__ == '__main__':
    app.run(debug=True)


