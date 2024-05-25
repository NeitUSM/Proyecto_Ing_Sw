from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.core.cache import cache
import time


# Create your views here.
# Define a constant for the maximum number of login attempts
MAX_LOGIN_ATTEMPTS = 3
# Define a constant for the lockout duration in seconds
LOCKOUT_DURATION = 180  # 5 minutes

def base(request):
    return render(request, 'base.html')

def loginview(request):
    if request.method == 'GET':
        return render(request, 'login.html', {
            'form': AuthenticationForm()
        })
    else:
        username = request.POST['username']
        password = request.POST['password']
        
        # Check if the user is currently locked out
        lockout_key = f"login_lockout_{username}"
        if cache.get(lockout_key):
            return render(request, 'login.html',{
                'form': AuthenticationForm(), 
                'error': 'Su cuenta está bloqueada temporalmente. Por favor, inténtelo de nuevo más tarde.'
            })

        user = authenticate(request, username=username, password=password)
        attempts_key = f"login_attempts_{username}"
        if user is None:
            # Increment the login attempts counter
            attempts = cache.get(attempts_key, 0) + 1
            cache.set(attempts_key, attempts, timeout=LOCKOUT_DURATION)

            if attempts >= MAX_LOGIN_ATTEMPTS:
                # If maximum attempts reached, lock the account
                cache.set(lockout_key, True, timeout=LOCKOUT_DURATION)
                return render(request, 'login.html',{
                    'form': AuthenticationForm(), 
                    'error': 'El correo o contraseña es incorrecto. Su cuenta ha sido bloqueada temporalmente.'
                })
            else:
                return render(request, 'login.html',{
                    'form': AuthenticationForm(), 
                    'error': 'El correo o contraseña es incorrecto'
                })
        
        else:
            # If login successful, reset the login attempts counter
            cache.delete(attempts_key)
            login(request, user)
            return redirect('base')