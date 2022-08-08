from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=10)

    def __str__(self):
        return f" Cliente: {self.nombre} {self.apellido}. Numero: {self.phone}. Email: {self.email}"

class Articulo(models.Model):
    nombre = models.CharField(max_length=30)
    seccion = models.CharField(max_length=30)
    precio = models.IntegerField()

    def __str__(self):
        return f"Articulo de nombre: {self.nombre}, perteneciente a la categoria: {self.seccion}, de valor: {self.precio}"

class Pedido(models.Model):
    numero = models.IntegerField()
    fecha = models.DateField()
    entregado = models.BooleanField()

    def __str__(self):
        return f"Pedido número: {self.numero}, realizado en la fecha: {self.fecha}, estado de estrega: {self.entregado}"
