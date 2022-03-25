from contextlib import redirect_stderr
from ctypes.wintypes import HLOCAL
from django.shortcuts import render, redirect
from django.http import HttpResponse
import MotoDinamicApp

from MotoDinamicApp.models import TipoProducto
from .forms import inputTipoProducto


def index(request):
    return HttpResponse("Hola, Bienvenidos a Moto Dinamic.")
    

# Create your views here.
def insertarTipoProducto(request):
    if request.method == 'GET':
        form = inputTipoProducto()
        return render(request, 'MotoDinamicApp/crearProducto.html',{'form': form})
    elif request.method == 'POST':
        #print(myTipoProducto)
        myTipoProducto = inputTipoProducto(request.POST)
        if myTipoProducto.is_valid():
            myTipoProducto.save()
        return redirect('insertar')
    return HttpResponse("funcion insertar")

def getTipoProducto(request):
    if request.method == "GET":
        return render(request, 'MotoDinamicApp/searchTipoProducto.html')
    if request.method == 'POST':
        myId = request.POST['productId']
        myTipoProducto = TipoProducto.objects.get(id = myId)
        return HttpResponse(myTipoProducto.nombre)

#def showTipoProduct(request)