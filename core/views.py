from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.db import IntegrityError
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home.html')

def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm()
        })
    else:
        # Autenticar usuario
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            # Verificar si el usuario existe
            if not User.objects.filter(username=request.POST['username']).exists():
                return render(request, 'signin.html', {
                    'form': AuthenticationForm(),
                    'error': 'El usuario no está registrado'
                })
            else:
                return render(request, 'signin.html', {
                    'form': AuthenticationForm(),
                    'error': 'contraseña incorrecta'
                })
        
        # Iniciar sesión exitosamente
        login(request, user)
        return redirect('home')
