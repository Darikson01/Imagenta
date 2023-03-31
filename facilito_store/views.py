from django.shortcuts import render
from django.shortcuts import redirect

from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.http import Http404
from django.core.paginator import Paginator
from django.db.models import Q
from .forms import ProductoForm, ComprasForm
from compras.models import Compras
from orders.models import Order
from carts.models import Cart
#from django.contrib.auth.models import User
from users.models import User

from .forms import RegisterForm

from products.models import Product

def index(request):
   return render(request, 'index.html',{
   
    })

def about(request):
    return render(request, 'about.html', {

    })

def list_produc(request):

    products = Product.objects.all().order_by('-id')

    return render(request,'producto.html', {
        'message': 'Listado de productos',
        'title': 'Productos',
        'products': products,
    })

@login_required(login_url='login')
def listarCompras(request):
    busqueda = request.POST.get("buscador")
    lista_compras = Compras.objects.order_by('producto')
    page = request.GET.get('page', 1)
    if busqueda:
        lista_compras= Compras.objects.filter(
            Q(producto = busqueda) 
            ).distinct()

    try:
        paginator = Paginator(lista_compras, 6)
        lista_compras = paginator.page(page)
    except:
        raise Http404

    data = {'entity': lista_compras,
            'title': 'LISTADO DE COMPRAS',
            'paginator': paginator
            }
    return render(request,'compras/listar.html',data)

@login_required(login_url='login')
def addcompra(request):
    data = {
        'form' : ComprasForm()
    }

    if request.method == 'POST':
        formulario = ComprasForm(data=request.POST, files=request.FILES)

        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Registro agregado correctamente")
            return redirect(to="listarcompras")
        else:
            data["form"] = formulario   
    return render(request, 'compras/agregar.html', data)

@login_required(login_url='login')

@login_required(login_url='login')
def editarCompra(request, id):
    compra = get_object_or_404(Compras, id=id)
    data = {
        'form': ComprasForm(instance=compra)
    }

    if request.method == 'POST':
        formulario = ComprasForm(data=request.POST, instance=compra, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Registro modificado correctamente")
            return redirect(to="listarproductos")
        data["form"] = formulario
    return render(request, 'compras/modificar.html', data)


@login_required(login_url='login')
def deleteCompra(request, id):
    compra = get_object_or_404(Compras, id=id)
    compra.delete()
    messages.success(request, "Registro eliminado correctamente")
    return redirect(to="listarcompras")


@login_required(login_url='login')
def listarProductos(request):
    busqueda = request.POST.get("buscador")
    lista_prouctos = Product.objects.order_by('title')
    page = request.GET.get('page', 1)
    if busqueda:
        lista_prouctos= Product.objects.filter(
            Q(title__icontains = busqueda) 
            ).distinct()

    try:
        paginator = Paginator(lista_prouctos, 6)
        lista_prouctos = paginator.page(page)
    except:
        raise Http404

    data = {'entity': lista_prouctos,
            'title': 'INVENTARIO',
            'paginator': paginator
            }
    return render(request,'productos/listar.html',data)

@login_required(login_url='login')
def addProducto(request):
    data = {
        'form' : ProductoForm()
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)

        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Registro agregado correctamente")
            return redirect(to="listarproductos")
        else:
            data["form"] = formulario   
    return render(request, 'productos/agregar.html', data)

@login_required(login_url='login')
def editarProducto(request, id):
    producto = get_object_or_404(Product, title=id)
    data = {
        'form': ProductoForm(instance=producto)
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Registro modificado correctamente")
            return redirect(to="listarproductos")
        data["form"] = formulario
    return render(request, 'productos/modificar.html', data)

@login_required(login_url='login')
def deleteProducto(request, id):
    producto = get_object_or_404(Product, id=id)
    producto.delete()
    messages.success(request, "Registro eliminado correctamente")
    return redirect(to="listarproductos")



def login_view(request):
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        username = request.POST.get('username') #diccionario
        password = request.POST.get('password') #None

        user = authenticate(username=username, password=password)#None
        if user:
            login(request, user)
            messages.success(request, 'Bienvenido {}'.format(user.username))

            if request.GET.get('next'):
                return HttpResponseRedirect(request.GET['next'])

            return redirect('producto')
        else:
            messages.error(request, 'Usuario o contraseña no validos')

    return render(request, 'users/login.html', {

    })

def logout_view(request):
    logout(request)
    messages.success(request, 'Sesión cerrada exitosamente')
    return redirect('index')

def register(request):
    

    form = RegisterForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():

        user = form.save()
        if user:
            login(request, user)
            messages.success(request, 'Usuario creado exitosamente')
            return redirect('producto')

    return render(request, 'users/register.html', {
        'form': form
    })

def contacto(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        subject = request.POST['subject']
        message = request.POST['message']
        
        template = render_to_string('email_template.html', {
            'name': name,
            'email': email,
            'phone': phone,
            'subject': subject,
            'message': message
        })
    
        email = EmailMessage(
            subject,
            template,
            settings.EMAIL_HOST_USER,
            ['imagentacontacto@gmail.com']
        )
        messages.success(request, "Gracias por su mensaje")
        email.fail_silently = False
        email.send()
    
    return render(request, 'contacto.html',{

    })
    

@login_required(login_url='login')
def listarPedidos(request):
    busqueda = request.POST.get("buscador")
    lista_pedido = Order.objects.order_by('user')
    page = request.GET.get('page', 1)
    if busqueda:
        lista_pedido= Order.objects.filter(
            Q(user = busqueda) 
            ).distinct()

    try:
        paginator = Paginator(lista_pedido, 6)
        lista_pedido = paginator.page(page)
    except:
        raise Http404

    data = {'entity': lista_pedido,
            'title': 'LISTADO DE PEDIDOS',
            'paginator': paginator
            }
    return render(request,'pedidos/listar.html',data)

@login_required(login_url='login')

def listarVentas(request):
    busqueda = request.POST.get("buscador")
    lista_ventas = Cart.objects.order_by('user')
    page = request.GET.get('page', 1)
    if busqueda:
        lista_ventas= Cart.objects.filter(
            Q(user = busqueda) 
            ).distinct()

    try:
        paginator = Paginator(lista_ventas, 6)
        lista_ventas = paginator.page(page)
    except:
        raise Http404

    data = {'entity': lista_ventas,
            'title': 'LISTADO DE VENTAS',
            'paginator': paginator
            }
    return render(request,'ventas/listar.html',data)