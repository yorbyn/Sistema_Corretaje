from django.shortcuts import render


def iniciar_sesion(request):
    return render(request, 'CRM/sesiones/iniciar_sesion.html')

def crear_cuenta(request):
    return render(request, 'CRM/sesiones/crear_cuenta.html')


def listar_propiedades(request):
    return render(request, 'CRM/propiedades/listar_propiedades.html')

def registrar_propiedades(request):
    # Aquí procesaremos el formulario POST más adelante
    return render(request, 'CRM/propiedades/registrar_propiedades.html')

def detalle_propiedades(request, id):
    return render(request, 'CRM/propiedades/detalle_propiedades.html')


def listar_propietarios(request):
    return render(request, 'CRM/propietarios/listar_propietarios.html')

def registrar_propietario(request):
    return render(request, 'CRM/propietarios/registrar_propietario.html')