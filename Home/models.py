from django.db import models

class Property(models.Model):
    owner_name = models.CharField(max_length=150)
    location = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    land_photo = models.ImageField(upload_to='property_photos/')

    def __str__(self):
        return self.owner_name
