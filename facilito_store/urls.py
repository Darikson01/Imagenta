from django.contrib import admin

from django.urls import path
from django.urls import include

from django.conf.urls.static import static
from django.conf import settings

from . import views
from products.views import ProductListView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.index, name='index'),
    path('producto', ProductListView.as_view(), name='producto'),
    path('contact', views.contacto, name='contacto'),
    path('about', views.about, name='about'),
    path('compras/listar',views.listarCompras, name='listarcompras'),
    path('compras/agregar', views.addcompra, name='addcompra'),
    path('deleteCompra/<id>/', views.deleteCompra, name='deleteCompra'),
    path('editCompra/<id>/', views.editarCompra, name='editCompra'),
    path('productos/listar',views.listarProductos, name='listarproductos'),
    path('productos/agregar', views.addProducto, name='addproducto'),
    path('editProducto/<id>/', views.editarProducto, name='editProducto'),
    path('deleteProducto/<id>/', views.deleteProducto, name='deleteProducto'),
    path('usuarios/login', views.login_view, name='login'),
    path('usuarios/logout', views.logout_view, name='logout'),
    path('usuarios/registro', views.register, name='register'),
    path('admin/', admin.site.urls),
    path('productos/', include('products.urls')),
    path('carrito/', include('carts.urls')),
    path('orden/', include('orders.urls')),
    path('direcciones/', include('shipping_addresses.urls')),
    path('codigos/', include('promo_codes.urls')),
    path('pagos/', include('billing_profiles.urls')),
    path('reset_password', auth_views.PasswordResetView.as_view(template_name="reset-password.html"), name='password_reset'),
    path('reset_password_send', auth_views.PasswordResetDoneView.as_view(template_name="reset-password-send.html"), name='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name="password-reset-confirm.html"), name='password_reset_confirm'),
    path('reset_password_complete', auth_views.PasswordResetCompleteView.as_view(template_name="password-reset-complete.html"), name='password_reset_complete'),
    path('pedidos/listar',views.listarPedidos, name='listarpedidos'),
    path('ventas/listar',views.listarVentas, name='listarventas'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
