from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import RegisterForm

from products.models import Product

'''def index(req):
    products = Product.objects.all().order_by('-id')

    context = {
        'message': 'Listado de productos',
        'title': 'Productos',
        'products': products,
    }

    return render(req, 'index.html', context)'''

def login_view(req):

    if req.user.is_authenticated:
        return redirect('index')

    if req.method == 'POST':
        username = req.POST.get('username')
        password = req.POST.get('password')
        
        # crea un objeto usuario si hay coinciencia con los datos
        # sino, le asigna null
        user = authenticate(username=username, password=password)

        if user:
            # genera la sesion del usuario con la peticion
            # y el objeto usuario
            login(req, user)

            # envia un mensaje de exito al logearse
            messages.success(req, 'Bienvenido {}'.format(user.username))

            # como parametro se pasa el nombre
            # asociado a la url
            return redirect('index')
        else:
            messages.error(req, 'Usuario o contraseña no válidos')
            return redirect('login')

    return render(req, 'users/login.html', {})

def logout_view(req):
    # para este punto, el objeto req
    # ya contiene la sesion
    logout(req)
    messages.success(req, 'Sesión cerrada exitosamente')
    return redirect('login')

def register(req):

    if req.user.is_authenticated:
        return redirect('index')

    # crea el formulario con los datos enviados por POST,
    # sino es POST, crea un formulario vacio
    form = RegisterForm(req.POST or None)

    # el metodo is_valid aplica las validaciones a cada campo
    # incluyendo aquellas definidas con el prefijo "clean"
    if req.method == 'POST' and form.is_valid():
        user = form.save()

        if user:
            login(req, user)
            messages.success(req, 'Usuario creado exitosamente')
            return redirect('index')

    context = {'form': form}
    return render(req, 'users/register.html', context)