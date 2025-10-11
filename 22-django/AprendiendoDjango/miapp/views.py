from django.shortcuts import render, HttpResponse, redirect

# Create your views here.



"""
- MVC = Modelo Vista Controlador
- MVT = Modelo Vista Template
En el MVT el controlador lo maneja Django y se le llama Vista (views.py)
"""
layout = """
<h1>Sitio Web con Django | Manuel Ríos</h1>
<hr/>
<ul>
    <li> <a href="/">Inicio</a> </li>
    <li> <a href="/hola-mundo/">Hola Mundo</a> </li>
    <li> <a href="/pagina/">Página</a> </li>
    <li> <a href="/contacto/">Contacto</a> </li>
</ul>
<hr/>


"""

def index(request):
    html = """
    <h1>Inicio</h1>
    <p> Años hasta el 2050</p>
    <ul>
    """

    year = 2024
    while year <= 2050:
        html += f"<li>{str(year)}</li>"
        year += 1
    html += "</ul>"
    return render(request, "index.html")

def hola_mundo(request):
    return render(request, "hola_mundo.html")

def pagina(request, redirigir=0):
    if redirigir == 1:
        return redirect('contacto', nombre="Manuel", apellidos="Ríos")
    return render(request, "pagina.html")

def contacto(request, nombre="", apellidos=""):
    html = "<h3>Sin datos de contacto</h3>"

    if nombre and apellidos:
        html = "El nombre completo es: "
        html += f"<h3>Contacto de {nombre} {apellidos}</h3>"
    return HttpResponse(layout + f"<h2>Contacto</h2>" + html)