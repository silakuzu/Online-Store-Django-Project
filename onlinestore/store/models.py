from django.db import models

# Create your models here.

class categories(models.Model):
    categoryID= models.CharField(max_length=100)
    categoryname = models.CharField(max_length=100)

