from django.urls import path
from . import views

urlpatterns = [
    path('', views.principal, name='home'),
    path('login/', views.login_juez, name='login'),
    path('inicio/', views.inicio, name='inicio'),
    path('horarios/', views.horario, name='horarios'),
]
