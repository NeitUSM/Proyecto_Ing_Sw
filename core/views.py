from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.


def base(request):
    return render(request, 'base.html')

def loginview(request):
    if request.method == 'GET':
        return render(request, 'login.html', {
            'form': AuthenticationForm()
        })
    else:
        user= authenticate(request, username= request.POST['username'], password= request.POST['password'])
        
        if user is None:
            return render(request, 'login.html',{
                "form": AuthenticationForm(), 
                "error":'El correo o contraseña es incorrecto'
            })
        
        else:
            login(request, user)
            return redirect('base')

        

    