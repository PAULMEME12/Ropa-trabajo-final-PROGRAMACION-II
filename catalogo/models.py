from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import login
from django.shortcuts import render, redirect

class Cliente(AbstractUser):
    # Puedes agregar otros campos personalizados aquí

    def __str__(self):
        return self.username

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre

class Compra(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha = models.DateField()
    productos = models.ManyToManyField(Producto, through='DetalleCompra')

    def __str__(self):
        return f"Compra {self.id} de {self.cliente.username}"

class DetalleCompra(models.Model):
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(null=False, blank=False)

def registrar_usuario(request):
    from .forms import RegistroForm
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegistroForm()
    return render(request, 'catalogo/registro.html', {'form': form})