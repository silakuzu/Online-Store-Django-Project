"""dprojx URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# dprojx/urls.py
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from dappx import views
from django.conf.urls.static import static
from dprojx import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$',views.index,name='index'),
    url(r'^special/',views.special,name='special'),
    url(r'^dappx/',include('dappx.urls')),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^details',views.details,name='details'),
    path('<int:product_id>/',views.details,name='details'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)