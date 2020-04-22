from django.contrib import admin


# dappx/admin.py

from dappx.models import UserProfileInfo,productcategories,products
# Register your models here.
admin.site.register(UserProfileInfo)
admin.site.register(products)
admin.site.register(productcategories)
# admin.site.register(userType)