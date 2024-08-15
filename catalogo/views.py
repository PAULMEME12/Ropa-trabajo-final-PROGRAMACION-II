from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Cliente, Producto, Compra, DetalleCompra
from .forms import  ProductoForm, CompraForm
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from .forms import RegistroForm,ClienteForm
from django.contrib.auth import login, authenticate
from django.contrib.auth import views as auth_views
from django.contrib import messages
from django.contrib.auth.views import LoginView
from .forms import DetalleCompraForm, CategoriaForm
from django.forms import inlineformset_factory

class LoginRegistroView(LoginView):
    template_name = 'catalogo/login.html'

@login_required
def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'catalogo/lista_clientes.html', {'clientes': clientes})

@login_required
def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'catalogo/lista_productos.html', {'productos': productos})

@login_required
def lista_compras(request):
    compras = Compra.objects.all().order_by('-fecha')
    return render(request, 'catalogo/lista_compras.html', {'compras': compras})

@login_required
def home(request):
    return render(request, 'catalogo/index.html')
# Agregar, editar y eliminar vistas para clientes, productos y compras

def registrar_usuario(request):
    if request.method == 'POST':
        form = RegistroForm (request.POST)
        print(form)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Cuenta creada para {username}!')
            return redirect('LoginRegistroView')
    else:
        form = RegistroForm ()
    return render(request, 'catalogo/registro.html', {'form': form})

@login_required
def nuevo_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')
    else:
        form = ClienteForm()
    return render(request, 'catalogo/form_cliente.html', {'form': form})

@login_required
def editar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'catalogo/form_cliente.html', {'form': form})

@login_required
def eliminar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    if request.method == 'POST':
        cliente.delete()
        return redirect('lista_clientes')
    return render(request, 'catalogo/confirmar_eliminar.html', {'obj': cliente})

# Vistas para Cliente
@login_required
def nuevo_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')
    else:
        form = ClienteForm()
    return render(request, 'catalogo/form_cliente.html', {'form': form})

@login_required
def editar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'catalogo/form_cliente.html', {'form': form})

@login_required
def eliminar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    if request.method == 'POST':
        cliente.delete()
        return redirect('lista_clientes')
    return render(request, 'catalogo/confirmar_eliminar.html', {'obj': cliente})

# Vistas para Producto
@login_required
def nuevo_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm()
    return render(request, 'catalogo/form_producto.html', {'form': form})

@login_required
def editar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'catalogo/form_producto.html', {'form': form})

@login_required
def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        producto.delete()
        return redirect('lista_productos')
    return render(request, 'catalogo/confirmar_eliminar.html', {'obj': producto})

# Vistas para Compra
@login_required
def nueva_compra(request):
    if request.method == 'POST':
        print(request.POST)  # Agrega esta línea para verificar los datos enviados
        form = DetalleCompraForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_compras')
    else:
        form = DetalleCompraForm()
    return render(request, 'catalogo/form_compra.html', {'form': form})

@login_required
def editar_compra(request, id):
    compra = get_object_or_404(Compra, id=id)
    if request.method == 'POST':
        form = CompraForm(request.POST, instance=compra)
        if form.is_valid():
            form.save()
            return redirect('lista_compras')
    else:
        form = CompraForm(instance=compra)
    return render(request, 'catalogo/form_compra.html', {'form': form})

@login_required
def eliminar_compra(request, id):
    compra = get_object_or_404(Compra, id=id)
    if request.method == 'POST':
        compra.delete()
        return redirect('lista_compras')
    return render(request, 'catalogo/confirmar_eliminar.html', {'obj': compra})


def detalle_compra(request, compra_id):
    compra = get_object_or_404(Compra, id=compra_id)
    return render(request, 'catalogo/detalle_compra.html', {'compra': compra})

def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')  # Redirige a una vista que liste las categorías
    else:
        form = CategoriaForm()
    return render(request, 'catalogo/crear_categoria.html', {'form': form})


def crear_compra(request):
    DetalleCompraFormSet = inlineformset_factory(Compra, DetalleCompra, form=DetalleCompraForm, extra=1, can_delete=True)
    
    if request.method == 'POST':
        compra_form = CompraForm(request.POST)
        formset = DetalleCompraFormSet(request.POST)
        
        if compra_form.is_valid() and formset.is_valid():
            compra = compra_form.save(commit=False)
            compra.cliente = request.user  # Asumiendo que el cliente es el usuario autenticado
            compra.save()
            
            for form in formset:
                detalle = form.save(commit=False)
                detalle.compra = compra
                detalle.save()
            
            return redirect('lista_compras')  # Redirige a una vista que liste las compras
    else:
        compra_form = CompraForm()
        formset = DetalleCompraFormSet()
    
    return render(request, 'catalogo/crear_compra.html', {
        'compra_form': compra_form,
        'formset': formset,
    })