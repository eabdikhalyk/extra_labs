from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    description = models.TextField()
    quantity = models.IntegerField()
    category_id = models.IntegerField()
    is_active = models.BooleanField()

class Category(models.Model):
    name = models.CharField(max_length=255)