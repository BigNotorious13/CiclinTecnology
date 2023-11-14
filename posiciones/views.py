from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
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


def agregar_equipo(request):
    data = {
        'form': EquipoForm()
    }

    # Agregar la informción que se envio
    if request.method == 'POST':
        # Crear el formulario con los datos enviados
        formulario = EquipoForm(data=request.POST)
        # Validar la información
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = 'Equipo guardado'
        else:
            data['form'] = formulario
    return render(request, 'equipos/agregar.html', data)


def modificar_equipo(request, clv):
    equipo = get_object_or_404(Equipo, clv=clv)
    data = {
        'form': EquipoForm(instance=equipo)
    }
    # Si el usuarioya dijo que si, POST
    if request.method == 'POST':
        formulario = EquipoForm(data=request.POST, instance=equipo)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Equipo Actualizado")
            return redirect(to='equipos')
        # Si no es valido
        data['form'] = formulario
    return render(request, 'equipos/modificar.html', data)


def eliminar_equipo(request, clv):
    equipo = get_object_or_404(Equipo, clv=clv)
    equipo.delete()
    messages.success(request, "Equipo Eliminado")
    return redirect(to='equipos')


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


def equipos(request):
    equi = Equipo.objects.all()
    data = {
        'titulos': ['ID', 'CIUDAD', 'NOMBRE', 'CANTIDAD COMP.', 'ACCIONES'],
        'equipos': equi
    }
    return render(request, 'Equipos.html', context=data)
