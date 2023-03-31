from django.contrib import admin

from .models import SaleDetail
from .models import Sale

admin.site.register(Sale)
admin.site.register(SaleDetail)