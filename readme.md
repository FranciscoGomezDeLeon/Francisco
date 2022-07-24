
This README would normally document whatever steps are necessary to get your application up and running.

Configuration
Para poner en marcha este repositorio previamente debera entrar a la carpeta "env/Scripts/" y ejecutar ./activate para iniciar entorno virtual.
Instalar complementos en el archivo requirements.txt desde la ubicacion "Francisco/myweb" con el comando "pip install -r requirements.txt".
Crear Usuario Admin si lo desea para obtener control total desde el siguiente comando.
python manage.py createsuperuser
Tambien puede crearse su superuser desde admin con el login previo nombre/Francisco contraseña/Francisco.
Si no lo desea puede registrarse desde la web

Luego sigue la siguiente linea de comandos.
py manage.py makemigrations
py manage.py migrate
py manage.py runserver 

What is this repository for?
Es una appweb con una tienda ecommerce.

Quick summary
Tienda en modo Admin/superuser:
Inicio
Categorias
Listado de categorias/modificar/eliminar/crearnueva
Productos/modificar/eliminar/crearproductosnuevos
Lstado de Productos
Nosotros
Contacto
Acerca de mi
Carrito
Usuario/crear/eliminar/darpermisos
En Modo User:
Inicio
Categorias
Listado de categorias/buscar
Productos
Listado de productos/buscar
Nosotros
Contacto
Acerca de mi
Carrito
Usuario/login

Version
Python 3.10.5
Django 4,0,6
Bootstrap4

How do I get set up?

Para poder comprar en la tienda necesitaras registrarte. (borde superior derecho)

Database configuration
Sqlite3

Writing tests
Los resultados se encuentran documentado en el archivo excel en la ubicacion /Francisco/test/casosdeprueba

Who do I talk to?
Francisco Gomez De Leon,Soluciones en Piscinas Uruguay, Canelones,Uruguay.
