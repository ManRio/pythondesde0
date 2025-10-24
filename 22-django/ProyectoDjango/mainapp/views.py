from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from mainapp.forms import RegisterForm
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def index(request):
    return render(request, "mainapp/index.html", {
        'title': 'Inicio'
        })

def about(request):
    return render(request, "mainapp/about.html", {
        'title': 'Sobre Nosotros'
        })

def register_page(request):

    if request.user.is_authenticated:
        return redirect('index')
    else:
        register_form = RegisterForm()

        if request.method == 'POST':
            register_form = RegisterForm(request.POST)
            if register_form.is_valid():
                register_form.save()
                messages.success(request, 'Usuario registrado correctamente')

                return index(request)

        return render(request, "mainapp/users/register.html", {
            'title': 'Registro de Usuario',
            'register_form': register_form
            })


def login_page(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.warning(request, 'Usuario o contraseña incorrecta')

        return render(request, "mainapp/users/login.html", {
            'title': 'Iniciar Sesión'
            })

def logout_user(request):
    logout(request)

    return redirect('login')
