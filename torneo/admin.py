from django.contrib import admin
from .models import Cliente, ClienteAdmin, Menu, MenuAdmin

#Registramos nuestras clases principales.
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Menu, MenuAdmin)
