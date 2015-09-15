from django.db import models

class Products(models.Model):
    id = models.IntegerField()
    product_name = models.CharField(max_length=30)
    product_code= models.CharField(max_length=30)
    price = models.IntegerField()
    available_quantity = models.IntegerField()
    created_date = models.DateField()
    updated_date = models.DateField() 
