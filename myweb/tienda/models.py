
from email.mime import image
from io import UnsupportedOperation
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Avatar(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='media/avatar', null=True, blank=True)
    
    class meta:
        verbose_name = "avatar"
        verbose_name_plural = "avatares"


class Categorias(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = "categorias"
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['id']


#modelo Productos
class Productos(models.Model):
    nombre = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='imgproductos/%Y/%m/%d', blank=True)
    descripcion = models.CharField(max_length=500)
    precio = models.IntegerField()
    stock = models.IntegerField(null=True, default=0)
    categoria = models.ForeignKey(Categorias, on_delete=models.PROTECT)
    oferta = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'productos'
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['id']


class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    mensaje = models.TextField()

    def __str__(self):
        return self.nombre
    class Meta:
        db_table = 'contacto'
        verbose_name = 'Contacto'
        verbose_name_plural = 'Contactos'
        ordering = ['nombre']
        
class Mensaje(models.Model):
    user = models.TextField()
    mensaje = models.TextField()
    fecha = models.DateTimeField()
    
    def __str__(self):
        return self.user
    class Meta:
        db_table = 'mensaje'
        verbose_name = 'Mensaje'
        verbose_name_plural = 'Mensajes'
        ordering = ['fecha']


# Model Carrito

