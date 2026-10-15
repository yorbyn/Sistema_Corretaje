from django.urls import path
from . import views

urlpatterns = [

    path('', views.listar_propiedades, name='home'),
    # Login y Crear Cuenta
    path('login/', views.iniciar_sesion, name='iniciar_sesion'),
    path('registro/', views.crear_cuenta, name='crear_cuenta'),
    # Propiedades
    path('propiedades/', views.listar_propiedades, name='listar_propiedad'),
    path('propiedades/nueva/', views.registrar_propiedades, name='registrar_propiedad'),
    path('propiedades/<int:id>/', views.detalle_propiedades, name='detalle_propiedad'),
   # Propietarios
    path('propietarios/', views.listar_propietarios, name='listar_propietario'),
    path('propietarios/nuevo/', views.registrar_propietario, name='registrar_propietario'),
]