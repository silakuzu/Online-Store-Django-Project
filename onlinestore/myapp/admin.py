from django.contrib import admin
from .models import products
from .models import productcategories
from .models import userType
from .models import users
from .models import orderdetails
from .models import orders


admin.site.register(productcategories)
admin.site.register(products)
admin.site.register(userType)
admin.site.register(users)
admin.site.register(orderdetails)
admin.site.register(orders)


