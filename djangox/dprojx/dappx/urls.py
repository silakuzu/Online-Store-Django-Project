# dappx/urls.py
from django.conf.urls import url
from dappx import views
from django.urls import path
from django.conf.urls.static import static
from dprojx import settings

# SET THE NAMESPACE!
app_name = 'dappx'
# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    url(r'^register/$',views.register,name='register'),
    url(r'^user_login/$',views.user_login,name='user_login'),
    url(r'^index/$',views.index,name='index'),
    url(r'^details/(?P<product_id>\d+)/$',views.details,name='details'),
    url(r'^search/$', views.search, name='search'),
    url(r'^category/(?P<category_name>.*)/$', views.category, name='category'),
    #url(r'^search/(?P<increasing_filter>.*)/$', views.search, name='search'),
    url(r'^increasingprice/(?P<increasing_filter>.*)/$', views.increasing, name='increasing'),
    url(r'^decreasingprice/(?P<decreasing_filter>.*)/$', views.decreasing, name='decreasing'),
    url(r'^ascending/(?P<ascending_filter>.*)/$', views.ascending, name='ascending'),
    url(r'^descending/(?P<descending_filter>.*)/$', views.descending, name='descending'),

    #url(r'^cart/$', views.cart, name='cart'),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)