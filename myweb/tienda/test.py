from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from tienda.models import Contacto, Productos, Categorias

class Productostest(TestCase):

    def setup(self):
        Productos.objects.create(nombre = 'Alguicida', descripcion = 'Alguicida', precio = '10', stock = '10', categoria = '1', oferta = 'True',comentarios = 'hola')
        
    def test_producto_nombre(self):
        producto = Productos.objects.get(nombre = 'Alguicida', descripcion = 'Alguicida', precio = '10', stock = '10', categoria = '1', oferta = 'True',comentarios = 'hola')
        self.assertEqual(producto.nombre, 'Alguicida')
        
class ContactoTest(TestCase):
    
    def setup(self):
         Contacto = Contacto.objects.create(nombre = 'Juan', correo = '', mensaje = 'Hola')
    
    def test_contacto_nombre(self):
            contacto = Contacto.objects.get(nombre = 'Juan', correo = '', mensaje = 'Hola')
            self.assertEqual(contacto.nombre, 'Juan')

class CategoriasTest(TestCase):
    
    def setup(self):
         Categorias.objects.create(nombre = 'Piletas de fibra')
    
    def test_categoria_nombre(self):
            categoria = Categorias.objects.get(nombre = 'Piletas de fibra')
            self.assertEqual(categoria.nombre, 'Piletas de fibra')


