# dappx/forms.py
from django import forms
from dappx.models import UserProfileInfo
from django.contrib.auth.models import User
from dappx.models import products
import django_filters


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','password','email')
class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site','profile_pic')


class ProductFilter(django_filters.FilterSet):
    class Meta():
        model = products
        fields = ('name', 'brand', 'ShortDesc', 'LongDesc')