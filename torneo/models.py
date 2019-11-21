from django.db import models
from django.contrib import admin
# from PIL import Image

class Cliente(models.Model):
    nombre = models.CharField(max_length=30,default='')
    anio = models.IntegerField()
    # imagen = models.ImageField(default='')

    def __str__(self):
        return self.nombre


class Menu(models.Model):
    nombre = models.CharField(max_length=60)
    anio = models.IntegerField()
    personajes = models.ManyToManyField(Cliente, through='Mains')

    def __str__(self):
        return self.nombre

class Mains(models.Model):
    personaje = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    jugador = models.ForeignKey(Menu, on_delete=models.CASCADE)

class MainsInLine(admin.TabularInline):
    model = Mains

    extra = 1

class ClienteAdmin(admin.ModelAdmin):
    inlines = (MainsInLine,)

class MenuAdmin(admin.ModelAdmin):
    inlines = (MainsInLine,)
