from tkinter import Widget
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import RegistroUsuarioForm
import loginApp
from django.contrib.auth.models import User
from .forms import RegistroUsuarioForm

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('productos')
        else:
            messages.info(request,'Error al inciar sesión, intente de nuevo')
            return redirect('login')
    else:
        return render(request, 'authenticate/login.html',{})

def logout_user(request):
    logout(request)
    messages.info(request,'Salida con éxito')
    return redirect('login')

def register_user(request):
    if request.method == "POST":
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            username =  form.cleaned_data['username']
            password = form.cleaned_data['password1']
            messages.success(request, 'Registro exitoso')
            return redirect('registrar_usuario')
    else:
        form = RegistroUsuarioForm()

    return render(request,'authenticate/registrar_usuario.html',{'form':form,})

def modelimUsuario(request):
    usuarios = User.objects.all()
    if request.method == "GET":
        return render(request, 'authenticate/editarUsuario.html', {'usuarios': usuarios})
    if request.method == 'POST':
        myUser = request.POST['usuario']
        miUsuario = User.objects.get(username = myUser)
        return render(request, 'authenticate/editarUsuario.html', {'usuario': miUsuario , 'usuarios': usuarios})

def eliminarUsuario(request, pk):
    usuario = User.objects.get(username = pk)
    if request.method == 'GET':
        return render(request, 'authenticate/eliminarUsuario.html', {'usuario': usuario})
    if request.method == 'POST':
        usuario.delete()
        return redirect('buscar_usuario')

    