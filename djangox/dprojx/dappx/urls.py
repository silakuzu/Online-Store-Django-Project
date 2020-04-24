# dappx/urls.py
from django.conf.urls import url
from dappx import views
from django.urls import path

# SET THE NAMESPACE!
app_name = 'dappx'
# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    url(r'^register/$',views.register,name='register'),
    url(r'^user_login/$',views.user_login,name='user_login'),
    url(r'^index/$',views.index,name='index'),
    url(r'^details/$',views.details,name='details'),
    url(r'^search/$', views.search, name='search'),
    url(r'^cart/$', views.cart, name='cart'),
    url(r'^category/$', views.search, name='category'),

]