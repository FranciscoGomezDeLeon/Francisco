from django.contrib import admin
from .models import *
from django.contrib.auth.models import User

# Register your models here.

class User(admin.ModelAdmin):
    list_display= ['username', 'email', 'first_name', 'last_name', 'is_staff', 'avatar']
    list_editable= ['username', 'email', 'first_name', 'last_name', 'is_staff', 'avatar']
    search_fields= ['username', 'email']

class ProductoAdmin(admin.ModelAdmin):
    list_display = ["nombre", "precio", "categoria","stock"]
    list_editable = ["precio"]
    search_fields = ["nombre","stock"]
    list_filter = ["categoria"]
    list_per_page = 10
    

admin.site.register(Categorias,)
admin.site.register(Productos, ProductoAdmin)
admin.site.register(Contacto)
admin.site.register(Mensaje)
admin.site.register(Avatar)

