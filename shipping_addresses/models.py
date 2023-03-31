from django.db import models

from users.models import User

class ShippingAddress(models.Model):
    user = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    line1 = models.CharField(max_length=200)
    line2 = models.IntegerField(max_length=200, blank=True)
    OPCIONES_CHOICES = (
        ('Armenia', 'Armenia'),
        ('Barrancabermeja', 'Barrancabermeja'),
        ('Barranquilla', 'Barranquilla'),
        ('Bogotá', 'Bogotá'),
        ('Bucaramanga', 'Bucaramanga'),
        ('Buga', 'Buga'),  
        ('Cali', 'Cali'),
        ('Chía', 'Chía'),
        ('Cúcuta', 'Cúcuta'),  
        ('Duitama', 'Duitama'),
        ('Girardot', 'Girardot'),
        ('Honda', 'Honda'),  
        ('Ibagué', 'Ibagué'),
        ('Ipiales', 'Ipiales'),
        ('Jamundí', 'Jamundí'),  
        ('Leticia', 'Leticia'),
        ('Manizales', 'Manizales'),
        ('Mariquita', 'Mariquita'),  
        ('Medellín', 'Medellín'),
        ('Mompox', 'Mompox'),
        ('Montería', 'Montería'),  
        ('Murillo', 'Murillo'),
        ('Neiva', 'Neiva'),
        ('Pasto', 'Pasto'),  
        ('Pereira', 'Pereira'),
        ('San Andrés', 'San Andrés'),
        ('Santa Marta', 'Santa Marta'),  
        ('Valledupar', 'Valledupar'),
        ('Barranquila', 'Barranquila'),  
        ('Villavicencio', 'Villavicencio'),
        ('Zipaquirá', 'Zipaquirá'),
        
    )
    city = models.CharField(max_length=50, choices=OPCIONES_CHOICES)
    state = models.CharField(max_length=100)
    reference = models.CharField(max_length=300)
    postal_code = models.IntegerField(max_length=6, null=False, blank=False) #zip
    default = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.postal_code

    def has_orders(self):
        return self.order_set.count() >= 1

    def update_default(self, default=False):
        self.default = default
        self.save()

    @property
    def address(self):
        return '{} - {}'.format(self.city, self.state)

