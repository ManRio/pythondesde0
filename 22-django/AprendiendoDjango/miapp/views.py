from django.shortcuts import render, HttpResponse, redirect
from miapp.models import Article
from django.db.models import Q
from miapp.forms import FormArticle
from django.contrib import messages

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
    """
    html = ""
    <h1>Inicio</h1>
    <p> Años hasta el 2050</p>
    <ul>
    ""

    year = 2024
    while year <= 2050:
        html += f"<li>{str(year)}</li>"
        year += 1
    html += "</ul>"
    """
    year = 2024
    hasta = range(year, 2051)

    nombre = "Manuel Ríos"
    lenguajes = ['Python', 'JavaScript', 'Java', 'C++', 'C#', 'PHP']

    return render(request, "index.html", {
        'title': 'Inicio',
        'mi_variable': 'soy un dato que esta en la vista',
        'nombre': nombre,
        'lenguajes': lenguajes,
        'years': hasta
        })

def hola_mundo(request):
    return render(request, "hola_mundo.html")

def pagina(request, redirigir=0):
    if redirigir == 1:
        return redirect('contacto', nombre="Manuel", apellidos="Ríos")
    return render(request, "pagina.html", {
        'texto': '',
        'lista': ['uno', 'dos', 'tres', 'cuatro', 'cinco']
    })

def contacto(request, nombre="", apellidos=""):
    html = "<h3>Sin datos de contacto</h3>"

    if nombre and apellidos:
        html = "El nombre completo es: "
        html += f"<h3>Contacto de {nombre} {apellidos}</h3>"
    return HttpResponse(layout + f"<h2>Contacto</h2>" + html)

def crear_articulo(request, title, content, public):
    articulo = Article(
        title= title,
        content= content,
        public= public
    )
    articulo.save()

    return HttpResponse(f"Articulo creado: <strong>{articulo.title}</strong> - {articulo.content}")

def create_full_article(request):
    if request.method == "POST":
        formulario = FormArticle(request.POST)

        if formulario.is_valid():
            data_form = formulario.cleaned_data

            title = data_form.get('title')
            content = data_form.get('content')
            public = data_form.get('public')

            articulo = Article(
                title= title,
                content= content,
                public= public
            )
            articulo.save()

            #return HttpResponse(f"Artículo creado: {articulo.title} - {articulo.content} - {articulo.public}")

            #Crear mensaje flash
            messages.success(request, f"Artículo creado correctamente: {articulo.id} - {articulo.title} - {articulo.content}")

            return redirect('articulos')
    else:
        formulario = FormArticle()

    return render(request, "create_full_article.html", {
        'form': formulario
    })

def articulo(request):
    try:
        articulo = Article.objects.get(title="Superman", public=True)
        response = (f"Artículo: <br/> {articulo.title} - {articulo.content}")
    except Article.DoesNotExist:
        response = "<h1>El artículo no existe</h1>"
    return HttpResponse(response)

def editar_articulo(request, id):
    articulo = Article.objects.get(pk=id)
    articulo.title = "Batman"
    articulo.content = "Pelicula de Batman"
    articulo.public = True
    articulo.save()
    return HttpResponse(f"Artículo editado: <br/> {articulo.title} - {articulo.content}")

def articulos(request):
    articulos = Article.objects.filter(public=True).order_by('-id')
    return render(request, "articulos.html", {
        'articulos': articulos
    })

def borrar_articulo(request, id):
    articulo = Article.objects.get(pk=id)
    articulo.delete()
    return redirect('articulos')

def save_article(request):

    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']
        public = request.POST['public']

        if not title or not content or public is None:
            return HttpResponse("<h2>Faltan campos</h2>", status=400)

        # convertir '1'/'0' a booleano
        public = bool(int(public))

        articulo = Article(
            title= title,
            content= content,
            public= public
        )
        articulo.save()

        #return HttpResponse(f"Articulo creado: <strong>{articulo.title}</strong> - {articulo.content}")
        return redirect('articulos')
    else:
        return HttpResponse("<h2>No se ha podido crear el artículo</h2>")

def create_article(request):
    return render(request, "create_article.html")


