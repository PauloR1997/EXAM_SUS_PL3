from django.shortcuts import render, HttpResponse, redirect
from django.db.models import Q
from django.contrib import messages
# Create your views here.
layout = """
    <h1> susti lp3 || </h1>
    <hr/>
    <ul>
        <li>
            <a href="/inicio">Inicio</a>
        </li>
    </ul>
    <hr/>
"""

def index(request):

    return render(request, 'index.html', {
        'titulo': 'Inicio',
    })

    
def listar_region(request):

    return render(request, 'listar_region.html',{

    })


def create_full_region(request):
    return render(request, 'create_full_region.html',{

    })

def listar_empleado(request):

    return render(request, 'listar_empleado.html',{

    })


def create_full_empleado(request):
    return render(request, 'create_full_empleado.html',{

    })