from django.contrib import admin
from django.urls import path, include
from gestion_pedidos import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')),
    path('busqueda/', views.busqueda_productos),
    path('buscar/', views.buscar),
    path('contacto/', views.contacto),
]
