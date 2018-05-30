"""p_django_tmall URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url, include
# from django.contrib import admin
import xadmin

urlpatterns = [
    # url('admin/', admin.site.urls),
    url(r'xadmin/', xadmin.site.urls),
    url(r'^art/', include('art.urls')),

    # url('account/', include('auth01.urls')),
    # url('day4_28/', include('day4_28.urls')),
    # url(r'^$', views.index),
    # url('', views.get_cate)
]
