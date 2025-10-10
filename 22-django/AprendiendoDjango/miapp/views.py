from django.shortcuts import render, HttpResponse

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
    return HttpResponse(layout + html)

def hola_mundo(request):
    return HttpResponse(layout + """
        <h1>Hola Mundo con Django!!</h1>
        <h3>Soy Manuel Ríos</h3>
        <p>Esto es mi primera web con Django</p>
        <p>Estamos en el curso de Master en Python</p>
    """)

def pagina(request):
    return HttpResponse(layout + """
        <h1>Página de mi web</h1>
        <p>Creado por Manuel Ríos</p>
    """)