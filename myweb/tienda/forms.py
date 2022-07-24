from django import forms
from .models import Contacto, Mensaje, Productos, Categorias, Avatar
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class MensajeForm(forms.ModelForm):
    
    class Meta:
        model = Mensaje
        widgets={
            'mensaje': forms.Textarea(attrs={
                'rows':5,
                'cols':30
                }),
        }
        fields = '__all__'

class ConctactoForm(forms.ModelForm):

    class Meta:
        model = Contacto
        widgets={
            'mensaje': forms.Textarea(attrs={
                'rows':5,
                'cols':30
                }),
        }
        fields = '__all__'


class ProductoForm(forms.ModelForm):

    class Meta:
        model = Productos
        fields = ["nombre", "descripcion", "precio", "stock", "categoria", "oferta", "imagen"]
        

class CategoriaForm(forms.ModelForm):

    class Meta:
        model = Categorias
        fields = ["nombre"]

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(max_length=30, required=True)
    first_name = forms.CharField(label="Nombre", required=False)
    last_name = forms.CharField(label="Apellido", required=False)
    email = forms.EmailField(label="Email")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput) # la contraseña no se vea
    password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput)
   
  

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

        #help_texts = {k:"" for k in fields}

class UserEditForm(UserCreationForm):

    username = forms.CharField(label="username")
    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")
    email = forms.EmailField(label="Email")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput, required=False)
    password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput, required=False)
    
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}

class AvatarForm(forms.Form):
    imagen = forms.ImageField(label="Imagen", required=False)

    class Meta:
        model = Avatar
        fields = ['imagen']
        
        
    
        
