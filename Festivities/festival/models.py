from django.db import models
from datetime import date
from django.contrib.auth.models import User

class Location(models.Model):
    address = models.CharField(max_length=100)
    longititude = models.DecimalField(max_digits = 8, decimal_places = 5, null=True, blank=True)
    lattidude = models.DecimalField(max_digits = 8, decimal_places = 5, null=True, blank=True)

    def __str__(self): 
        return self.address
    
    class Meta:
        app_label = 'festival'

class Festivities(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    start_date = models.DateField(default=date.today)
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    location = models.ForeignKey(Location, on_delete = models.CASCADE )

    def __str__(self):
        return self.name
    
    class Meta:
        app_label = 'festival'

class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    message = models.TextField(max_length = 500)
    created_at = models.DateField(auto_now_add=True)
    festivities = models.ForeignKey(Festivities, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    
    class Meta:
        app_label = 'festival'

class Handicraft(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
    price = models.DecimalField(max_digits = 6, decimal_places = 2, null=True, blank=True)
    location = models.ForeignKey(Location, on_delete = models.CASCADE )

    def __str__(self):
        return self.name
    
    class Meta:
        app_label = 'festival'

class Calender(models.Model):
    event = models.ForeignKey(Festivities,on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
    
    class Meta:
        app_label = 'festival'