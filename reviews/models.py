from django.db import models
from products.models import Product

class Review(models.Model):
    review_text = models.CharField(max_length=2000)
    rating = models.IntegerField()
    name = models.CharField(max_length=255)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)