from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.core.exceptions import ValidationError
from django.contrib import messages
from .models import CartProducts
from products.models import Product
from .utils import get_or_create_cart

def cart(request):
    cart = get_or_create_cart(request)
    
    return render(request, 'carts/cart.html', {
        'cart': cart
    })

def add(request):
    cart = get_or_create_cart(request)
    product = Product.objects.get(pk=request.POST.get('product_id'))
    quantity = int(request.POST.get('quantity', 1))
    messages.success(request, 'Producto añadido correctamente al carrito')

    if product.stock < quantity:
        messages.error(request, 'No hay suficiente stock para agregar {0} unidades al carrito'.format(quantity))
        return redirect(request.META['HTTP_REFERER'])

    cart_product = CartProducts.objects.create_or_update_quantity(cart=cart, product=product, quantity=quantity)

    new_stock = product.stock - quantity
    product.stock = new_stock
    product.save()

    return render(request, 'carts/add.html', {
        'quantity': quantity,
        'product': product,
        'cart_product': cart_product,
    })

def remove(request):
    cart = get_or_create_cart(request)
    product = get_object_or_404(Product, pk=request.POST.get('product_id'))

    

    p = cart.cartproducts_set.get(product_id = request.POST.get('product_id'))
    product.stock = product.stock + p.quantity
    product.save()

    messages.success(request, 'Producto eliminado correctamente')
    cart.products.remove(product)
    messages


    return redirect('carts:cart')
