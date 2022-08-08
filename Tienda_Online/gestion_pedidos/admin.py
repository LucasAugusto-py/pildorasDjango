from django.contrib import admin
from .models import Cliente, Articulo, Pedido
# Register your models here.

class ClienteAdmin(admin.ModelAdmin):
    list_display=("nombre","apellido","email","phone")
    search_fields=("nombre","apellido")

class ArticulosAdmin(admin.ModelAdmin):
    list_filter = ("seccion", )

class PedidosAdmin(admin.ModelAdmin):
    list_filter = ("fecha",)
    date_hierarchy = "fecha"
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Articulo, ArticulosAdmin)
admin.site.register(Pedido, PedidosAdmin)