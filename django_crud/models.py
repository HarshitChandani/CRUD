from django.db import models

# Create your models here.
class Product(models.Model):
   name = models.CharField(max_length=100,null=False)
   price = models.IntegerField(null=True)
   qty = models.IntegerField(null=False)
