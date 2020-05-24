from django.contrib import admin


# dappx/admin.py

from dappx.models import UserProfileInfo,productcategories,products,orders,cartItem,cartTable
# Register your models here.
admin.site.register(UserProfileInfo)
admin.site.register(products)
admin.site.register(productcategories)
admin.site.register(orders)
admin.site.register(cartTable)
admin.site.register(cartItem)
# admin.site.register(userType)