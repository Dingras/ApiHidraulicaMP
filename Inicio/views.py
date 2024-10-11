from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import CustomAuthenticationForm ,CustomUserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return redirect('menu')
    
    if request.method == 'GET':
        return render(request, 'form_login.html', {'form':CustomAuthenticationForm})
    else:
        try:
            usuario = authenticate(request, username = request.POST['username'], password=request.POST['password'] )
            if usuario != None:
                login(request, usuario)
                return redirect('menu')
            else:
                return render(request, 'form_login.html', {'form':CustomAuthenticationForm},{'error':'Las datos ingresados son incorrectos.'})
        except:
            return render(request, 'form_login.html', {'form':CustomAuthenticationForm},{'error':'Las datos ingresados son incorrectos.'})

def salir(request):
    logout(request)
    return redirect('/')

@login_required(login_url='/')
def register(request):
    if request.method == 'GET':
        return render(request, 'form_register.html',{'form':CustomUserCreationForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                usuario = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                usuario.save()
                return render(request, 'form_login.html',{'menssage': 'Usuario creado con exito.'})
            except:
                return render(request, 'form_register.html',{'form':CustomUserCreationForm , 'error':'Usuario existente.'})
        else:
            return render(request, 'form_register.html',{'form':CustomUserCreationForm , 'error':'Las contraseñas no coinciden.'})

@login_required(login_url='/')
def users_view(request):
    data_users = User.objects.order_by('id')
    return render(request, 'users.html',{'users':data_users})