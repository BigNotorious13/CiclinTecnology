from django.urls import path
from . import views

urlpatterns = [
    path('', views.principal, name='home'),
    path('login/', views.login_juez, name='login'),
    path('inicio/', views.inicio, name='inicio'),
    path('horarios/', views.horario, name='horarios'),
    path('posiciones/', views.posiciones, name='posiciones'),
    path('resultados/', views.resultados, name='resultados'),
    path('categorias/elite/', views.categoria_elite, name='cate_elite'),

    path('categorias/femenil/', views.categoria_femenil, name='cate_femenil'),
    path('categorias/master30', views.categoria_master30, name='cate_master30'),
    path('categorias/master40', views.categoria_master40, name='cate_master40'),

    path('equipos/agregar/', views.agregar_equipo, name='agregar_equipo'),
    path('equipos/modificar/<int:clv>', views.modificar_equipo, name='modificar_equipo'),
    path('equipos/eliminar/<int:clv>', views.eliminar_equipo, name='eliminar_equipo'),
    path('equipos/', views.equipos, name='equipos'),
]
