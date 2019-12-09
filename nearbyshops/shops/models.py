from django.contrib.gis.db import models

# Create your models here.
class Shop(models.Model):
    name = models.CharField(max_length=100)
    location = models.PointField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    def __str__(self):
        shop_attrs = self.name, self.location,  self.address, self.city
        for attr in shop_attrs:
            return attr