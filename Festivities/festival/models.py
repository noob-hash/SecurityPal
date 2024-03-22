from django.db import models

class Location(models.Model):
    address = models.CharField(max_length=100)
    longititude = models.DecimalField(max_digits = 5, decimal_places = 2, null=True, blank=True)
    lattidude = models.DecimalField(max_digits = 5, decimal_places = 2, null=True, blank=True)

    def __str__(self): 
        return self.address
    
    class Meta:
        app_label = 'festival'
# Create your models here.
class Festivities(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    Location = models.ForeignKey(Location, on_delete = models.CASCADE )

    def __str__(self):
        return self.name
    
    class Meta:
        app_label = 'festival'