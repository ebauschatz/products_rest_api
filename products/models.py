from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    inventory_quantity = models.IntegerField()
    image_link = models.CharField(max_length=1000, null=True)