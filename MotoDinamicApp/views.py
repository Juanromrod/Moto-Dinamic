from ctypes.wintypes import HLOCAL
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hola, Bienvenidos a Moto Dinamic.")
    

# Create your views here.
