from django.shortcuts import render, redirect
from .models import Crud
from django.contrib import messages



def home(request):
    obj = Crud()
    datos = obj.datos()
    contexto = {
        'departamentos': datos
    }
    return render(request, 'home.html', contexto)


def insertar(request):
    if request.method != 'POST':
        return render(request, 'insertar.html')
    else:
        num = request.POST['num']
        nom = request.POST['nom']
        loc = request.POST['loc']
        obj = Crud()
        obj.insertar(num, nom, loc)

    messages.success(request, "¡Se ha creado un nuevo departamento!")
    return redirect('home')


def editar(request):
    if request.method != 'POST':
        num = request.GET['num']
        return render(request, 'editar.html', {'valor': num})
    elif request.method == 'POST':
        num = request.POST['num']
        nom = request.POST['nom']
        loc = request.POST['loc']
        obj = Crud()
        obj.actualizar(nom, loc, num)

    messages.success(request, "¡El departamento se ha editado correctamente!")
    return redirect('home')


def eliminar(request):
    num = request.GET['num']
    obj = Crud()
    obj.eliminar(num)

    messages.success(request, "¡El departamento se ha eliminado correctamente!")
    return redirect('home')