from django.shortcuts import render


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
    return render(request, 'inicio.html')


def horario(request):
    return render(request, 'horarios/horario.html')


def categoria_elite(request):
    return render(request, 'categoria/elite.html')


def categoria_femenil(request):
    return render(request, 'categoria/femenil.html')


def categoria_master30(request):
    return render(request, 'categoria/master30.html')


def categoria_master40(request):
    return render(request, 'categoria/master40.html')


def equipo_constru(request):
    return render(request, 'equipos/constru.html')
