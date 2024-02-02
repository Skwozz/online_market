from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    SECTION = [('PR', 'provider'), ('CL', 'client')]
    type_user = models.CharField(max_length=2, choices=SECTION, default=SECTION[1][0])


class Warehouse(models.Model):
    name = models.CharField(max_length=64)


class Product(models.Model):
    name = models.CharField(max_length=128)
    quantity = models.IntegerField()
    warehouse = models.ForeignKey(Warehouse, related_name="products", on_delete=models.CASCADE)


class Purchase(models.Model):
    product = models.ForeignKey(Product, related_name="purchase", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="purchase", on_delete=models.CASCADE)
