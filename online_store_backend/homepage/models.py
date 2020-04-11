from django.db import models


class products (models.Model):
    name = models.CharField(max_length=100)
    id = models.AutoField(primary_key=True)
    CategoryID = models.IntegerField()
    brand = models.CharField(max_length=100)
    price = models.FloatField()
    Quantity = models.CharField(max_length=100)
    ShortDesc = models.CharField(max_length=100)
    LongDesc = models.CharField(max_length=100)

    stock = models.FloatField(max_length=100)
    Location = models.CharField(max_length=100)

class productcategories (models.Model):
    CategoryID =  models.IntegerField()
    CategoryName = models.CharField(max_length=100)

class  orderdetails (models.Model):
    DetailID = models.IntegerField()
    orderID = models.IntegerField()
    productID =  models.IntegerField()
    name = models.CharField(max_length=100)
    price = models.FloatField(max_length=100)
    sku = models.CharField(max_length=100)
    quantity = models.IntegerField()

class orders (models.Model):
    ID = models.IntegerField()
    userID = models.IntegerField()
    amount = models.FloatField(max_length=100)
    shipName =  models.CharField(max_length=100)
    shipAddress =  models.CharField(max_length=100)
    city =  models.CharField(max_length=100)
    zip =  models.CharField(max_length=100)
    country  = models.CharField(max_length=100)
    phone =  models.CharField(max_length=100)
    shipping = models.FloatField(max_length=100)
    email =  models.CharField(max_length=100)
    date = models.DateField()
    shipped = models.IntegerField()

class users (models.Model):
    ID =  models.IntegerField()
    type = models.CharField(max_length=100)
    email =  models.CharField(max_length=100)
    password =   models.CharField(max_length=100)
    firstname =  models.CharField(max_length=100)
    lastname =  models.CharField(max_length=100)
    city =  models.CharField(max_length=100)
    zip =  models.CharField(max_length=100)
    registrationDate = models.DateField()
    ip =   models.CharField(max_length=100)
    phone =  models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    address =  models.CharField(max_length=100)


class userType (models.Model):
    typeID = models.IntegerField()
    type = models.CharField(max_length=100)