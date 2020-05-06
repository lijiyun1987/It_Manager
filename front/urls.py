"""it_manage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from django.urls import path, re_path
from . import views


urlpatterns = [
    # path('', views.index, name='index'),
    # path('mac/', views.mac, name='mac'),
    # re_path(r'mac/search/', views.mac_search, name='mac_search'),
    # re_path(r'ajax/search/', views.ajax_search, name='ajax_search'),
    # path('login/', views.acc_login, name='login'),
    # path('logout/', views.acc_logout, name='logout'),
    # path('ops/', views.ops, name='ops'),
    # path('addops/', views.addops, name='addops'),
    # path('mainten/', views.mainten, name='mainten'),
    # path('addmainten/', views.addmainten, name='addmainten'),
    # re_path(r'^mac/(?P<year>[0-9]{4})/$', views.mac, name='mac'),
    # path('', views.detail_mac, name='detail'),
    # path('addreplace/', views.addreplace, name='addreplace'),
    # path('addmac/', views.addmac, name='addmac'),
    # path('check/', views.CheckView.as_view(), name='check'),
    # path('login/', views.login, name='login'),
]
