from django.db import models
from products.models import Product
from proveedor.models import supplier
from django.db.models.signals import post_save
from django.dispatch import receiver

class Compras(models.Model):
    producto = models.ForeignKey(Product, on_delete=models.CASCADE)
    proveedor = models.ForeignKey(supplier, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    total = models.IntegerField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.producto) 
    
    class Meta:
        verbose_name = 'Compra'
        verbose_name_plural = 'Compras'
        db_table = 'Compras'
        ordering = ['producto']

@receiver(post_save, sender=Compras)
def actualizar_stock(sender, instance, **kwargs):
    producto = instance.producto
    cantidad = instance.cantidad
    producto.stock += cantidad
    producto.save()

     
