from django.shortcuts import render
from posiciones.models import Categoria, Carrera, Equipo, Competidor
from posiciones.forms import CategoriaForm, CarreraForm, EquipoForm, CompetidorForm


# Create your views here.
def principal(request):
    return render(request, 'principal.html')


def posiciones(request):

    return render(request, 'posiciones/posicion.html')


def resultados(request):
    return render(request, 'resultados/resultado.html')


def login_juez(request):
    return render(request, 'iniJuez.html')


def inicio(request):
    categorias = Categoria.objects.all()
    # Diccionario con las categorias
    data = {
        'categorias': categorias
    }
    return render(request,
                  'horarios/horario.html',
                  context=data)


def agregar_categoria(request):
    data = {
        'form': CategoriaForm()
    }

    # Agregar la informción que se envio
    if request.method == 'POST':
        # Crear el formulario con los datos enviados
        formulario = CategoriaForm(data=request.POST)
        # Validar la información
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = 'Categoria guardada'
        else:
            data['form'] = formulario
    return render(request, 'categoria/agregar.html', data)


def horario(request):
    categorias = Categoria.objects.all()
    # Diccionario con las categorias
    data = {
        'categorias': categorias
    }
    return render(request,
                  'horarios/horario.html',
                  context=data)


def categoria_elite(request):
    competidor = Competidor.objects.all()
    data = {
        'competidores': competidor
    }
    return render(request, 'categoria/elite.html', context=data)


def categoria_femenil(request):
    competidor = Competidor.objects.all()
    data = {
        'competidores': competidor
    }
    return render(request, 'categoria/elite.html', context=data)


def categoria_master30(request):
    competidor = Competidor.objects.all()
    data = {
        'competidores': competidor
    }
    return render(request, 'categoria/elite.html', context=data)


def categoria_master40(request):
    competidor = Competidor.objects.all()
    data = {
        'competidores': competidor
    }
    return render(request, 'categoria/elite.html', context=data)


def equipo_constru(request):
    equipos = Equipo.objects.all()
    data = {
        'equipos': equipos
    }
    return render(request, 'equipos/constru.html', context=data)
