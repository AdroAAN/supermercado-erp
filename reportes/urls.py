from django.urls import path
from . import views

app_name = 'reportes'          # único lugar donde definimos el namespace

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    # aquí irán futuras rutas de reportes…
]
