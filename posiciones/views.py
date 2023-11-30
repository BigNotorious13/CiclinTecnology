from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from posiciones.models import Categoria, Carrera, Equipo, Competidor
from posiciones.forms import CategoriaForm, CarreraForm, EquipoForm, CompetidorForm
from django.views.generic import ListView


# VISTAS BASADAS EN CLASES
class CarreraListView(ListView):
    template_name = 'carreras/carreras_list.html'
    model = Carrera
    context_object_name = 'carreras'
    paginate_by = 5


class EquiposListView(ListView):
    template_name = 'equipos_vistaclase.html'
    model = Equipo
    context_object_name = 'equipos'
    paginate_by = 5


# FIN DE LAS VISTAS BASADAS EN CLASES


# Create your views here.
def principal(request):
    return render(request, 'principal.html')


def posiciones(request):
    return render(request, 'posiciones/posicion.html')


def resultados(request):
    return render(request, 'resultados/resultado.html')


def login_juez(request):
    return render(request, 'iniJuez.html')


# def inicio(request):
#   categorias = Categoria.objects.all()
# Diccionario con las categorias
#  data = {
#   'categorias': categorias
# }
# return render(request,
#             'carreras/carreras_list.html',
#             context=data)


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


def modificar_equipo(request, id_equipo):
    equipo = get_object_or_404(Equipo, id_equipo=id_equipo)
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


def eliminar_equipo(request, id_equipo):
    equipo = get_object_or_404(Equipo, id_equipo=id_equipo)
    equipo.delete()
    messages.success(request, "Equipo Eliminado")
    return redirect(to='equipos')


def equipos(request):
    equi = Equipo.objects.all()
    data = {
        'titulos': ['ID', 'CIUDAD', 'NOMBRE', 'CANTIDAD COMP.', 'ACCIONES'],
        'equipos': equi
    }
    return render(request, 'Equipos.html', context=data)


def categorias(request):
    cate = Categoria.objects.all()
    data = {
        'titulos': ['ID', 'NOMBRE', 'REQUISITOS', 'ACCIONES'],
        'categorias': cate
    }
    return render(request, 'categorias.html', context=data)


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


def modificar_categoria(request, id_categoria):
    cate = get_object_or_404(Categoria, id_categoria=id_categoria)
    data = {
        'form': CategoriaForm(instance=cate)
    }
    # Si el usuarioya dijo que si, POST
    if request.method == 'POST':
        formulario = CategoriaForm(data=request.POST, instance=cate)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Categoria Actualizada")
            return redirect(to='categorias')
        # Si no es valido
        data['form'] = formulario
    return render(request, 'categoria/modificar.html', data)


class CategoriaListView(ListView):
    template_name = 'categorias_vistaclase.html'
    model = Categoria
    context_object_name = 'categorias'
    paginate_by = 5


def eliminar_categoria(request, id_categoria):
    cate = get_object_or_404(Categoria, id_categoria=id_categoria)
    cate.delete()
    messages.success(request, "Categoria Eliminada")
    return redirect(to='categorias')
