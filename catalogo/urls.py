# catalogo/urls.py
from django.urls import path
from .views import   lista_clientes, lista_productos, lista_compras, home,registrar_usuario,LoginRegistroView, detalle_compra,crear_categoria,crear_compra
from . import views

urlpatterns = [
    
    path('home/', home, name='home'),
    # path('login/', login_registro, name='login_registro'),
    path('clientes/', lista_clientes, name='lista_clientes'),
    path('clientes/nuevo/', views.nuevo_cliente, name='nuevo_cliente'),
    path('clientes/editar/<int:id>/', views.editar_cliente, name='editar_cliente'),
    path('clientes/eliminar/<int:id>/', views.eliminar_cliente, name='eliminar_cliente'),
    path('productos/', lista_productos, name='lista_productos'),
    path('productos/nuevo/', views.nuevo_producto, name='nuevo_producto'),
    path('productos/editar/<int:id>/', views.editar_producto, name='editar_producto'),
    path('productos/eliminar/<int:id>/', views.eliminar_producto, name='eliminar_producto'),
    path('compras/', lista_compras, name='lista_compras'),
    path('compras/nuevo/', views.crear_compra, name='crear_compra'),
    path('compras/<int:compra_id>/', detalle_compra, name='detalle_compra'),
    path('registro/', registrar_usuario, name='registro'),
    path('categorias/nueva/', crear_categoria, name='crear_categoria'),
    path('', LoginRegistroView.as_view(), name='LoginRegistroView'),
    
    # Otras rutas de tu aplicación
]