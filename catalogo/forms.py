from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Cliente, Producto, Compra, DetalleCompra, Categoria

class RegistroForm(UserCreationForm ):
    class Meta:
        model = Cliente
        fields = ['username', 'email', 'password1', 'password2']

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'categoria', 'precio']

class CompraForm(forms.ModelForm):
    class Meta:
        model = Compra
        fields = [ 'fecha']
        widgets = {
            'fecha': forms.DateInput(attrs={
                'type': 'text',  # Esto permite que el navegador muestre un selector de fecha
                'class': 'form-control datepicker'  # Asegúrate de que tenga clases para estilos
            }),
        }

class DetalleCompraForm(forms.ModelForm):
    class Meta:
        model = DetalleCompra
        fields = ['producto', 'cantidad']  

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'

class CompraForm(forms.ModelForm):
    class Meta:
        model = Compra
        fields = '__all__'

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre']