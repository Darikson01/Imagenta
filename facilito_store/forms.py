from django import forms

#from django.contrib.auth.models import User
from users.models import User
from products.models import Product
from compras.models import Compras

class ProductoForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ["title", "description", "price","stock", "image"]
        labels = {
            'title': 'Nombre del Producto',
            'description': 'Description del Producto',
            'price': 'Precio',
            'stock': 'Unidades del producto',
            'image': 'Imagen'
            
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['title'].widget.attrs.update({
            'class': 'form-control'
        }) #Dic

        self.fields['description'].widget.attrs.update({
            'class': 'form-control'
        }) 
        self.fields['price'].widget.attrs.update({
            'class': 'form-control'
        })     
        self.fields['stock'].widget.attrs.update({
            'class': 'form-control'
        })   

class ComprasForm(forms.ModelForm):

    class Meta:
        model = Compras
        fields = ["producto", "proveedor", "cantidad","total"]        
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['producto'].widget.attrs.update({
            'class': 'form-control'
        }) #Dic

        self.fields['proveedor'].widget.attrs.update({
            'class': 'form-control'
        }) 
        self.fields['cantidad'].widget.attrs.update({
            'class': 'form-control'
        })     
        self.fields['total'].widget.attrs.update({
            'class': 'form-control'
        })  

       

class RegisterForm(forms.Form):
    username = forms.CharField( 
                                required=True,
                                min_length=4, max_length=50,
                                widget=forms.TextInput(attrs={
                                    'class': 'form-control',
                                    'id': 'username',
                                    'placeholder': 'Nombre de Usuario'
                                }))
   
    email = forms.EmailField( 
                                
                                required=True,
                                widget=forms.EmailInput(attrs={
                                    'class': 'form-control',
                                    'id': 'email',
                                    'placeholder': 'example@gamil.com'
                                }))
    password = forms.CharField( 
                                required=True,
                                widget=forms.PasswordInput(attrs={
                                    'id': 'password',
                                    'class': 'form-control',
                                    'placeholder': 'Contraseña'
                                }))
    password2 = forms.CharField(
                                required=True,
                                widget=forms.PasswordInput(attrs={
                                    'id': 'password',    
                                    'class': 'form-control',
                                    'placeholder': 'Confirmar Contraseña'
                                }))

    def clean_username(self):
        username = self.cleaned_data.get('username')

        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('El Nombre de Usuario ya se encuentra en uso')

        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('El email ya se encuentra en uso')

        return email

    def clean(self):
        cleaned_data = super().clean()

        if cleaned_data.get('password2') != cleaned_data.get('password'):
            self.add_error('password2', 'La Contraseña no coincide')

    def save(self):
        return User.objects.create_user(
                self.cleaned_data.get('username'),
                self.cleaned_data.get('email'),
                self.cleaned_data.get('password'),
            )
