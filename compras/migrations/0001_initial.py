# Generated by Django 4.0.2 on 2023-03-24 01:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0006_alter_product_stock'),
        ('proveedor', '0003_alter_supplier_address_alter_supplier_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compras',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField()),
                ('total', models.IntegerField()),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
                ('proveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proveedor.supplier')),
            ],
            options={
                'verbose_name': 'Compra',
                'verbose_name_plural': 'Compras',
                'db_table': 'Compras',
                'ordering': ['id'],
            },
        ),
    ]