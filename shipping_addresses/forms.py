from django.forms import ModelForm
from .models import ShippingAddress

class ShippingAddressForm(ModelForm):
    class Meta:
        model = ShippingAddress
        fields = [
            'line1', 'line2', 'city', 'state','postal_code', 'reference'
        ]
        labels = {
            'line1': 'Direccion',
            'line2': 'Numero de Telefono',
            'city': 'Ciudad',
            'state': 'Barrio',
            'postal_code': 'Código postal',
            'reference': 'Referencias'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['line1'].widget.attrs.update({
            'class': 'form-control',
            'required': True,
            
            
        }) #Dic

        self.fields['line2'].widget.attrs.update({
            'class': 'form-control',
            'required': True,
            'pattern': '[0-9]+',
        })

        self.fields['city'].widget.attrs.update({
            'class': 'form-control',
            'required': True,
            'pattern': '[a-zA-ZáéíóúÁÉÍÓÚñÑ ]+'
        })

        self.fields['state'].widget.attrs.update({
            'class': 'form-control',
            'pattern': '[a-zA-ZáéíóúÁÉÍÓÚñÑ ]+'
        })

        self.fields['postal_code'].widget.attrs.update({
            'class': 'form-control',
            'required': True,
            'pattern': '[0-6]',
            'placeholder': '0000'
        })

        self.fields['reference'].widget.attrs.update({
            'class': 'form-control',
            'required': True,
        })
