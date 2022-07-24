import email
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from .models import *
from .carro import Carro
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.views.generic import ListView, CreateView
from django.db.models import Q
from .forms import ConctactoForm, ProductoForm, CategoriaForm, UserRegisterForm, UserEditForm, AvatarForm, MensajeForm

    # Create your views here.
    
@login_required
def agregar_avatar(request):
    
    if request.method == "POST":
            
        form = AvatarForm(request.POST, request.FILES)

        if form.is_valid():

            user = User.objects.get(username=request.user.username) # usuario con el que estamos loggueados

            avatar = Avatar(usuario=user, imagen=form.cleaned_data["imagen"])

            avatar.save()

            # avatar = Avatar()
            # avatar.usuario = request.user
            # avatar.imagen = form.cleaned_data["imagen"]
            # avatar.save()

            return redirect("/")

    else:
        form = AvatarForm()
    
    return render(request,"Auth/agregar_avatar.html",{"form":form})
    
    # if request.method == "POST":
            
    #     form = AvatarForm(request.POST, request.FILES)

    #     if form.is_valid():
            
    #         user = user.objects.get(username=request.user.username)
    #         avatar = avatar.objects.get(usuario=user)
    #         avatar.image = info["image"]
    #         avatar.save()
    #         info = form.cleaned_data
        
    #         return render(request,"index.html")

    #     else:
    #         form = AvatarForm()
    
    # return render(request,"auth/agregaravatar.html")
    

def index(request):
    busqueda = request.POST.get("buscador")
    product_list = Productos.objects.order_by('nombre')
    page = request.GET.get('page', 1)

    if busqueda:
        product_list = Productos.objects.filter(
            Q(nombre__icontains = busqueda) |
            Q(descripcion__icontains = busqueda)
        ).distinct()
    
    try:
        paginator = Paginator(product_list, 12)
        product_list = paginator.page(page)
    except:
        raise Http404

    data = {'entity': product_list,
            'paginator': paginator
    }
    return render(request, 'index.html', data)


# Listar productos por categoria
def productoxCategoria(request, id):
    busqueda = request.POST.get("buscador")
    lista_productos = Productos.objects.filter(categoria = id)
    
    if busqueda:
        lista_productos = Productos.objects.filter(
            Q(nombre__icontains=busqueda) |
            Q(descripcion__icontains=busqueda)
        ).distinct()

    data = {'entity': lista_productos}
    return render(request, 'index.html', data)


# views productos
def detalleProducto(request, id):
    product = get_object_or_404(Productos, id=id)
    otrosProductos = Productos.objects.filter(categoria=product.categoria)
    data = {
        'producto': product,
        'productosRelacionados': otrosProductos
    }
    return render(request, 'producto/detalle.html', data)


@login_required(login_url='/login')
def addProducto(request):
    data = {
        'form' : ProductoForm()
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)

        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Registro agregado correctamente")
            return redirect(to="/listarproductos")
        else:
            data["form"] = formulario   
    return render(request, 'producto/agregar.html', data)


@login_required(login_url='/login')
def listarProductos(request):
    busqueda = request.POST.get("buscador")
    lista_productos = Productos.objects.order_by('nombre')
    page = request.GET.get('page', 1)
    if busqueda:
        lista_productos = Productos.objects.filter(
            Q(nombre__icontains = busqueda) |
            Q(descripcion__icontains = busqueda)
        ).distinct()

    try:
        paginator = Paginator(lista_productos, 6)
        lista_productos = paginator.page(page)
    except:
        raise Http404

    data = {'entity': lista_productos,
            'title': 'LISTADO DE PRODUCTOS',
            'paginator': paginator
            }
    return render(request, 'producto/listar.html', data)


@login_required(login_url='/login')
def editarProducto(request, id):
    producto = get_object_or_404(Productos, id=id)
    data = {
        'form': ProductoForm(instance=producto)
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Registro modificado correctamente")
            return redirect(to="/listarproductos")
        data["form"] = formulario
    return render(request, 'producto/modificar.html', data)


@login_required(login_url='/login')
def deleteProducto(request, id):
    producto = get_object_or_404(Productos, id=id)
    producto.delete()
    messages.success(request, "Registro eliminado correctamente")
    return redirect(to="/listarproductos")

def nosotros(request):
    return render(request, 'nosotros.html')

def acerca_de_mi(request):
    return render(request, 'acerca_de_mi.html')

def garantia(request):
    return render(request, 'garantia.html')

def devoluciones(request):
    return render(request, 'devoluciones.html')


# Views categorias
@login_required(login_url='/login')
def listCategorias(request):
    lista_categorias = Categorias.objects.all().order_by('nombre')
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(lista_categorias, 6)
        lista_categorias = paginator.page(page)
    except:
        raise Http404

    data = {'entity': lista_categorias,
            'title': 'LISTADO DE CATEGORIAS',
            'paginator': paginator
            }

    return render(request,'categorias.html', data)


@login_required(login_url='/login')
def addCategoria(request):
    data = {
        'form': CategoriaForm()
    }
    if request.method == 'POST':
        formulario = CategoriaForm(data=request.POST)

        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Registro agregado correctamente")
            return redirect(to="/categorias")
        else:
            data["form"] = formulario
    return render(request, 'categoria/agregar.html', data)


@login_required(login_url='/login')
def modificarCategoria(request, id):
    categoria = get_object_or_404(Categorias, id=id)

    data = {
        'form': CategoriaForm(instance=categoria)
    }
    if request.method == 'POST':
        formulario = CategoriaForm(data=request.POST, instance=categoria)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Registro modificado correctamente")
            return redirect(to="/categorias")
        else:
            data["form"] = formulario

    return render(request, 'categoria/modificar.html', data)


@login_required(login_url='/login')
def deleteCategoria(request, id):
    categoria = get_object_or_404(Categorias, id=id)
    categoria.delete()
    messages.success(request, "Registro eliminado correctamente")
    return redirect(to="/categorias")

def contacto(request):
    data = {
        'form': ConctactoForm()
    }

    if request.method == 'POST':
        formulario = ConctactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Gracias por su mensaje")
        else:
            data["form"] = formulario
    return render(request, 'contacto.html', data)

def mensaje(request):
    data = {
        'form': MensajeForm()
    }

    if request.method == 'POST':
        formulario = MensajeForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Gracias por su mensaje")
        else:
            data["form"] = formulario
    return render(request, 'Auth/mensaje.html', data)

def registrar(request):
    
    if request.method == "POST":
        
        form = UserRegisterForm(request.POST)
       
        if form.is_valid():

            username = form.cleaned_data.get('username')
            firstname = form.cleaned_data.get('firstname')
            lastname = form.cleaned_data.get('lastname')
            email = form.cleaned_data.get('email')
            password1 = form.cleaned_data.get('password1') 
            password2 = form.cleaned_data.get('password2')
            avatar = form.cleaned_data.get('avatar')
            
            form.save() 
            user = authenticate(username=username, password=password1)

            if user is not None:
                login(request, user)
                return render(request,"nosotros.html")

            else:
                return render(request,"Auth/registrar.html")


        return render(request,"Auth/registrar.html",{"form":form})
    
    form = UserRegisterForm()

    return render(request,"Auth/registrar.html",{"form":form})
            
    
                

@login_required
def editar_perfil(request):

    user = request.user 

    if request.method == "POST":
        
        form = UserEditForm(request.POST, instance=user)

        if form.is_valid():

            info = form.cleaned_data
            username = info["username"]
            user.first_name = info["first_name"]
            user.last_name = info["last_name"]
            user.email = info["email"]
            user.avatar = info["avatar"]

            user.save()

            return render(request,"nosotros.html",{"form":form})
    
    else:
        form = UserEditForm(initial={"email":user.email, "first_name":user.first_name, "last_name":user.last_name, "avatar":user.avatar})

    return render(request,"Auth/editar_perfil.html", {"form":form})

    

# Acciones carrito
def viewcart(request):
    return render(request, 'carrito/cart.html', {'carro': request.session['carro']})

def agregar_producto(request, producto_id):
    carro=Carro(request)
    producto=Productos.objects.get(id=producto_id)
    carro.agregar(producto=producto)
    return redirect(to="/viewcart")

def eliminar_producto(request, producto_id):
    carro=Carro(request)
    producto=Productos.objects.get(id=producto_id)
    carro.eliminar(producto=producto)
    return redirect(to="/viewcart")

def restar_producto(request, producto_id):
    carro = Carro(request)
    producto = Productos.objects.get(id=producto_id)
    carro.restar(producto=producto)
    return redirect(to="/viewcart")

def cleancart(request):
    carro=Carro(request)
    carro.limpiar_carro()
    return redirect(to="/viewcart")


def procesar_compra(request):
    messages.success(request, 'Gracias por su Compra!!')
    carro = Carro(request)
    carro.limpiar_carro()
    return redirect('/')


