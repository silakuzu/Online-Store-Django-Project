from django.db import models


class productcategories (models.Model):
    CategoryID =  models.AutoField(primary_key=True)
    CategoryName = models.CharField(max_length=100)

    def __str__(self):
        return self.CategoryID


class products (models.Model):
    name = models.CharField(max_length=100)
    product_id = models.AutoField(primary_key=True)
    Category_id = models.ForeignKey(productcategories, on_delete=models.CASCADE)
    productbrand = models.CharField(max_length=100)
    productprice = models.FloatField()
    Quantity = models.CharField(max_length=100)
    ShortDesc = models.CharField(max_length=100)
    LongDesc = models.CharField(max_length=100)

    stock = models.FloatField(max_length=100)
    Location = models.CharField(max_length=100)

    def __str__(self):
        return self.product_id


class userType (models.Model):
    typeID = models.AutoField(primary_key=True)
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.typeID


class users (models.Model):
    userID =   models.AutoField(primary_key=True)
    usertype = models.ForeignKey(userType, on_delete=models.CASCADE)
    email =  models.CharField(max_length=100)
    password =   models.CharField(max_length=100)
    firstname =  models.CharField(max_length=100)
    lastname =  models.CharField(max_length=100)
    city =  models.CharField(max_length=100)
    registrationDate = models.DateField()
    phone =  models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    address =  models.CharField(max_length=100)

    def __str__(self):
        return self.userID

class orders (models.Model):
    orderID = models.AutoField(primary_key=True)
    userID = models.ForeignKey(users, on_delete=models.CASCADE)
    amount = models.FloatField(max_length=100)
    shipName =  models.CharField(max_length=100)
    shipAddress =  models.CharField(max_length=100)
    city =  models.CharField(max_length=100)
    country  = models.CharField(max_length=100)
    phone =  models.CharField(max_length=100)
    shipping = models.FloatField(max_length=100)
    useremail =  models.CharField(max_length=100)
    orderdate = models.DateField()
    shipped = models.IntegerField()

    def __str__(self):
        return self.orderID

class  orderdetails (models.Model):
    DetailID = models.AutoField(primary_key=True)
    orderID = models.ForeignKey(orders, on_delete=models.CASCADE)
    productID = models.ForeignKey(products, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.FloatField(max_length=100)
    sku = models.CharField(max_length=100)
    quantity = models.IntegerField()

    def __str__(self):
        return self.DetailID


