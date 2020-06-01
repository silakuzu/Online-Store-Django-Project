from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import timedelta
from django.utils import timezone
from django.db.models import Sum

# Create your models here.
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    #portfolio_site = models.URLField(blank=True)
    #profile_pic = models.ImageField(upload_to='profile_pics',blank=True)
    #email =  models.CharField(max_length=100, null=True)
    age = models.IntegerField(null=True, blank=True)
    gender = models.CharField(max_length=20, null=True, blank=True)
    address =  models.CharField(max_length=100, null=True, blank=True)
    city =  models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    

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

#class orders (models.Model):
#    STATUS = (
#        ('New', 'New'),
#        ('Accepted', 'Accepted'),
#        ('Preparing', 'Preparing'),
#        ('OnShipping', 'OnShipping'),
#        ('Completed', 'Completed'),
#    )
#    orderID = models.AutoField(primary_key=True)
#    totalCost = models.FloatField(max_length=100)
#    shipName =  models.CharField(max_length=100)
#    shipAddress =  models.CharField(max_length=100)
#    billingAddress = models.CharField(max_length=100)
#    city =  models.CharField(max_length=100)
#    zip =  models.CharField(max_length=100)
#    country  = models.CharField(max_length=100)
#    state  = models.CharField(max_length=100)
#    email =  models.CharField(max_length=100)
#    date = models.DateField(auto_now=True)
#    status = models.IntegerField(choices=STATUS, default='New')

#def __str__(self):
#   return self.orderID

# class  orderdetails (models.Model):
#     orderdetailsID = models.AutoField(primary_key=True)
#     orderID = models.ForeignKey(orders,on_delete=models.CASCADE)
#     productID = models.ForeignKey(products, on_delete=models.SET_NULL, null=True)
#     quantity = models.IntegerField(default=1)
#     totalCost = models.FloatField()

# def __str__(self):
#     return self.orderdetailsID


class cartItem(models.Model):
    itemID = models.AutoField(primary_key=True)
    product = models.OneToOneField(products, on_delete=models.SET_NULL, null=True)
    itemquantity = models.IntegerField(default=1)#how much is added to the cart
    date_added = models.DateTimeField(auto_now=True)
    itemPrice = models.FloatField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    totalCost = models.FloatField(max_length=100,default=0)

    def set_itemPrice(self):
        self.itemPrice = (self.itemquantity)*(self.product.changedprice)
        return self.itemPrice

    def get_cart_total(self):
        self.totalCost = sum(self.all().itemPrice)
        return self.totalCost

    def __str__(self):
        return self.product.name




class orders (models.Model):
    orderID = models.AutoField(primary_key=True)
    STATUS = (
        ('New', 'New'),
        ('Accepted', 'Accepted'),
        ('Preparing', 'Preparing'),
        ('OnShipping', 'OnShipping'),
        ('Completed', 'Completed'),
    )
    details = models.ForeignKey(cartItem, null=True, on_delete=models.SET_NULL)
    status = models.CharField(choices=STATUS, max_length=160, default='New')
    date_created = models.DateTimeField(auto_now_add=True)

    def return_date_due():
        now = timezone.now()
        return now + timedelta(days=7)
    
    date_due = models.DateTimeField(default=return_date_due)

 

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
