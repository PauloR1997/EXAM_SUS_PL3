from django.shortcuts import render, HttpResponse, redirect
from django.db.models import Q
from miapp.forms import FormRegion
from django.contrib import messages
from miapp.models import Region
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
    regiones = Region.objects.all()
    """
    regiones = Region.objects.filter(
        Q(nombre__contains="Py") |
        Q(nombre__contains="Hab")
    )
    """
    return render(request, 'listar_region.html',{
        'regiones': regiones,
        'titulo': 'Listado de Regiones'
    })

def eliminar_region(request, id):
    region = Region.objects.get(pk=id)
    region.delete()
    return redirect('listar_region')

def save_region(request):
    if request.method == 'POST':
        codigo = request.POST['codigo']
        if len(codigo)<=3:
            return HttpResponse("<h2>El tamaño del codigo es pequeño, intente nuevamente</h2>")
        date = request.POST['date']
        name = request.POST['name']
        cases = request.POST['cases']
        deaths = request.POST['deaths']
        lethality = request.POST['lethality']

        region = region(
            date = date,
            name = name,
            cases = cases,
            deaths = deaths,
            lethality = lethality
        )
        region.save()
        return HttpResponse(f"Region Creada: {region.name} ")
    else:
        return HttpResponse("<h2> No se ha podido registrar la region </h2>")

def create_full_region(request):
    if request.method == 'POST':
        formulario1 = FormRegion(request.POST)
        if formulario1.is_valid():
            data_form = formulario1.cleaned_data
            date = data_form.get('date')
            name = data_form['name']
            cases = data_form['cases']
            deaths = data_form['deaths']
            lethality = data_form['lethality']
            region = Region(
                date = date,
                name= name,
                cases = cases,
                deaths = deaths,
                lethality = lethality
            )
            region.save()

            #Es para crear un mensaje Flash (Solo se muestra una vez)
            messages.success(request,f'Se agregó correctamente la region {region.id}')

            return redirect('listar_region')
    else:
        formulario1 = FormRegion()        
    return render(request, 'create_full_region.html',{
        'form': formulario1
    })

def listar_empleado(request):

    return render(request, 'listar_empleado.html',{

    })


def create_full_empleado(request):
    return render(request, 'create_full_empleado.html',{

    })