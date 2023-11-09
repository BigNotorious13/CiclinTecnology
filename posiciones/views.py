from django.template import loader
from django.http import HttpResponse


# Create your views here.
def principal(request):
    template = loader.get_template('principal.html')
    res = template.render(request=request)
    return HttpResponse(res)


def posiciones(request):
    template = loader.get_template('posiciones/posicion.html')
    res = template.render(request=request)
    return HttpResponse(res)


def resultados(request):
    template = loader.get_template('resultados/resultado.html')
    res = template.render(request = request)
    return HttpResponse(res)

def login_juez(request):
    template = loader.get_template('iniJuez.html')
    res = template.render(request=request)
    return HttpResponse(res)


data_horarios = {'titulos': ['Ubicacion', 'Horario', 'Categoria']}


def inicio(request):
    template = loader.get_template('horarios/horario.html')
    data = data_horarios
    res = template.render(data, request)
    return HttpResponse(res)


def horario(request):
    template = loader.get_template('horarios/horario.html')
    data = data_horarios
    res = template.render(data, request)
    return HttpResponse(res)


def categoria_elite(request):
    template = loader.get_template('categoria/elite.html')
    res = template.render(request= request)
    return HttpResponse(res)


def categoria_femenil(request):
    template = loader.get_template('categoria/femenil.html')
    res = template.render(request=request)
    return HttpResponse(res)


def categoria_master30(request):
    template = loader.get_template('categoria/master30.html')
    res = template.render(request=request)
    return HttpResponse(res)


def categoria_master40(request):
    template = loader.get_template('categoria/master40.html')
    res = template.render(request=request)
    return HttpResponse(res)


def equipo_constru(request):
    template = loader.get_template('equipos/constru.html')
    res = template.render(request=request)
    return HttpResponse(res)
