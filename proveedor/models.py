from django.db import models

class supplier(models.Model):
      name = models.CharField(max_length=25,verbose_name="Nombre del proveedor")
      phone = models.IntegerField(verbose_name="Telefono del proverdor",max_length=10)
      address = models.TextField(max_length=24,verbose_name="Direcion del proveedor ")

      def __str__(self):
          return self.name

      class Meta:
            verbose_name = 'Proveedor'
            verbose_name_plural = 'Proveedores'
            db_table = 'PROVEEDOR'
            ordering = ['id']
