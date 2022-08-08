from django.shortcuts import render
from django.http import HttpResponse
from .models import Cliente, Articulo, Pedido

# Create your views here.
def busqueda_productos(request):
    return render(request, 'busqueda.html')

def buscar(request):
    if request.GET['prd']:
        #mensaje=f"Artículo Busucado: {request.GET['prd']}"

        producto = request.GET['prd']
        if len(producto)>20:
            mensaje='Texto de busqueda demasiado largo'
        else:
            articulos = Articulo.objects.filter(nombre__icontains=producto)
            return render(request, "resultados.html", {'articulos':articulos, 'query':producto})
            
    else:
        mensaje = f"No has entroducido nada"
    return HttpResponse(mensaje)

def contacto(request):
    if request.method == 'POST':

        return render(request, 'gracias.html')

    return render(request, 'contacto.html')