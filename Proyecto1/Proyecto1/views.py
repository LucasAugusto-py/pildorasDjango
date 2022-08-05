from django.http import HttpResponse
import datetime
def saludo(request):
    return HttpResponse("Hola mundo con Django")

def despedida(request):
    return HttpResponse("Hasta luego Django")
def dameFecha(request):
    fecha_actual = datetime.datetime.now()
    documento = """
    <html>
    <body>
        <h1>
            Fecha y hora actuales %s
        </h1>
    </body>
    </html>"""% fecha_actual
    return HttpResponse(documento)

def calculaEdad(request,agno):
    edadActual = 18
    periodo = agno - 2022
    edadFutura = edadActual + periodo
    documento = """
    <html>
    <body>
        <h1>
           En el año %s tendras %s años
        </h1>
    </body>
    </html>"""%(agno, edadFutura)
    return HttpResponse(documento)