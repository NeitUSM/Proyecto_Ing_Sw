# views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from .form import CreateUserForm

def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cuenta creada exitosamente!')
            return redirect('exito') 
        else:
            messages.error(request, 'Por favor corrige los errores.')
    context = {'form': form}
    return render(request, 'core/register.html', context)

def exito(request):
    return render(request, 'core/exito.html')

def login(request):
    return render(request, 'core/login.html')