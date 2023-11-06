from django.shortcuts import render


# Create your views here.
def principal(request):
    return render(request, 'principal.html')


def login_juez(request):
    return render(request, 'iniJuez.html')


def inicio(request):
    return render(request, 'inicio.html')
def horario(request):
    return render(request, 'horarios/horario.html')
