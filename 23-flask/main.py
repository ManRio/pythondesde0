from flask import Flask, flash, redirect, url_for, render_template, request
from datetime import datetime
from flask_mysqldb import MySQL

app = Flask(__name__)

# 🔐 Clave secreta para sesiones/flash (dev: valor por defecto; prod: variable de entorno)
app.config['SECRET_KEY'] = 'dev-secret-no-usar-en-produccion'

# Conexion DB MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'proyectoflask'

mysql = MySQL(app)

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

@app.route('/crear-coche', methods=['GET', 'POST'])
def crear_coche():
    if request.method == 'POST':
        
        marca = request.form['marca']
        modelo = request.form['modelo']
        precio = request.form['precio']
        ciudad = request.form['ciudad']

        try:
            precio = float(precio)
        except ValueError:
            return "El precio debe ser un número válido", 400

         # Insertar en la base de datos
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO coches (marca, modelo, precio, ciudad) VALUES (%s, %s, %s, %s)", (marca, modelo, precio, ciudad))
        mysql.connection.commit()
        flash("Coche creado correctamente")
        cursor.close()

        return redirect(url_for('index'))

    return render_template("crear_coche.html")

@app.route('/coches')
def coches():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT id, marca, modelo, precio, ciudad FROM coches")
    coches = cursor.fetchall()
    cursor.close()
    return render_template("coches.html", coches=coches)

@app.route('/coche/<int:coche_id>')
def coche(coche_id):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM coches WHERE id = %s", (coche_id,))
    coche = cursor.fetchall()
    cursor.close()
    return render_template("coche.html", coche=coche[0])

@app.route('/borrar-coche/<int:coche_id>')
def borrar_coche(coche_id):
    cursor = mysql.connection.cursor()
    cursor.execute("DELETE FROM coches WHERE id = %s", (coche_id,))
    mysql.connection.commit()
    flash("Coche eliminado correctamente")
    cursor.close()
    return redirect(url_for('coches'))

@app.route('/editar-coche/<int:coche_id>', methods=['GET', 'POST'])
def editar_coche(coche_id):
    cursor = mysql.connection.cursor()
    if request.method == 'POST':
        marca = request.form['marca']
        modelo = request.form['modelo']
        precio = request.form['precio']
        ciudad = request.form['ciudad']

        try:
            precio = float(precio)
        except ValueError:
            flash("El precio debe ser un número válido", "danger")
            return redirect(url_for('editar_coche', coche_id=coche_id))

        cursor.execute(
            "UPDATE coches SET marca=%s, modelo=%s, precio=%s, ciudad=%s WHERE id=%s",
            (marca, modelo, precio, ciudad, coche_id)
        )
        mysql.connection.commit()
        cursor.close()
        flash("Coche actualizado correctamente", "success")
        return redirect(url_for('coches'))

    cursor.execute("SELECT id, marca, modelo, precio, ciudad FROM coches WHERE id=%s", (coche_id,))
    coche = cursor.fetchone()
    cursor.close()
    if not coche:
        flash("Coche no encontrado", "warning")
        return redirect(url_for('coches'))

    return render_template("crear_coche.html", coche=coche)

if __name__ == '__main__':
    app.run(debug=True)


