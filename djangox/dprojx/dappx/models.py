from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)
    def __str__(self):
        return self.user.username

class productcategories (models.Model):
    # STATUS = (
    #     (1,'True'),
    #     (0,'False'),
    # )
    CategoryName = models.CharField(max_length=100)

    def __str__(self):
        return self.CategoryName



# Create your models here.
class products (models.Model):
    # STATUS = (
    #     (1,'True'),
    #     (0,'False'),
    # )
    name = models.CharField(max_length=100)
    id = models.AutoField(primary_key=True)
    CategoryID = models.ForeignKey(productcategories,on_delete=models.CASCADE)
    brand = models.CharField(max_length=100)
    price = models.FloatField()
    Quantity = models.CharField(max_length=100)
    ShortDesc = models.CharField(max_length=100)
    LongDesc = models.CharField(max_length=100)
    image=models.ImageField(upload_to= 'foods')
    stock = models.FloatField(max_length=100)
    Location = models.CharField(max_length=100)
    changedprice = models.FloatField()

    def __str__(self):
        return self.name

class orders (models.Model):
    STATUS = (
        ('New', 'New'),
        ('Accepted', 'Accepted'),
        ('Preparing', 'Preparing'),
        ('OnShipping', 'OnShipping'),
        ('Completed', 'Completed'),
    )
    orderID = models.AutoField(primary_key=True)
    totalCost = models.FloatField(max_length=100)
    shipName =  models.CharField(max_length=100)
    shipAddress =  models.CharField(max_length=100)
    billingAddress = models.CharField(max_length=100)
    city =  models.CharField(max_length=100)
    zip =  models.CharField(max_length=100)
    country  = models.CharField(max_length=100)
    state  = models.CharField(max_length=100)
    email =  models.CharField(max_length=100)
    date = models.DateField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default='New')

def __str__(self):
    return self.orderID

# class  orderdetails (models.Model):
#     orderdetailsID = models.AutoField(primary_key=True)
#     orderID = models.ForeignKey(orders,on_delete=models.CASCADE)
#     productID = models.ForeignKey(products, on_delete=models.SET_NULL, null=True)
#     quantity = models.IntegerField(default=1)
#     totalCost = models.FloatField()

# def __str__(self):
#     return self.orderdetailsID

class cartTable(models.Model):
    cartID = models.AutoField(primary_key=True)

    def __str__(self):
        return self.cartID

class cartItem(models.Model):
    cartID = models.ForeignKey(cartTable, on_delete=models.CASCADE)
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    productID = models.ForeignKey(products,on_delete=models.CASCADE)

# class  orderdetails (models.Model):
#     DetailID = models.IntegerField()
#     orderID = models.IntegerField()
#     productID =  models.IntegerField()
#     name = models.CharField(max_length=100)
#     price = models.FloatField(max_length=100)
#     sku = models.CharField(max_length=100)
#     quantity = models.IntegerField()

# def __str__(self):
#     return self.orderID

# class orders (models.Model):
#     ID = models.IntegerField()
#     userID = models.IntegerField()
#     amount = models.FloatField(max_length=100)
#     shipName =  models.CharField(max_length=100)
#     shipAddress =  models.CharField(max_length=100)
#     city =  models.CharField(max_length=100)
#     zip =  models.CharField(max_length=100)
#     country  = models.CharField(max_length=100)
#     phone =  models.CharField(max_length=100)
#     shipping = models.FloatField(max_length=100)
#     email =  models.CharField(max_length=100)
#     date = models.DateField()
#     shipped = models.IntegerField()

# def __str__(self):
#     return self.ID

# class users (models.Model):
#     ID =  models.IntegerField()
#     type = models.CharField(max_length=100)
#     email =  models.CharField(max_length=100)
#     password =   models.CharField(max_length=100)
#     firstname =  models.CharField(max_length=100)
#     lastname =  models.CharField(max_length=100)
#     city =  models.CharField(max_length=100)
#     zip =  models.CharField(max_length=100)
#     registrationDate = models.DateField()
#     ip =   models.CharField(max_length=100)
#     phone =  models.CharField(max_length=100)
#     country = models.CharField(max_length=100)
#     address =  models.CharField(max_length=100)


# class userType (models.Model):
#     typeID = models.IntegerField()
#     type = models.CharField(max_length=100)


# def __str__(self):
#     return self.user.username
