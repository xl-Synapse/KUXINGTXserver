"""KUXINGTXserver URL Configuration

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
from django.contrib import admin
from django.urls import path

from server import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.loginPost, name='loginPost'),
    path('register/', views.registerPost, name='registerPost'),
    path('query_info/', views.query_infoPost, name='query_info'),
    path('modify_info/', views.modify_infoPost, name='modify_info'),
    path('relation_add/', views.relation_addPost, name='relation_add'),
    path('relation_confirm/', views.relation_confirmPost, name='relation_confirm'),
    path('relation_del/', views.relation_delPost, name='relation_del'),
    path('relation_my_all_qur/', views.relation_my_all_qurPost, name='relation_my_all_qur'),
    path('relation_my_one_qur/', views.relation_my_one_qurPost, name='relation_my_one_qur'),
    path('trends_my_add/', views.trends_my_addPost, name='trends_my_add'),
    path('trends_my_one_del/', views.trends_my_all_querPost, name='trends_my_one_del'),
    path('trends_my_all_del/', views.trends_my_all_querPost, name='trends_my_all_del'),
    path('trends_my_one_quer/', views.trends_my_all_querPost, name='trends_my_one_quer'),
    path('trends_my_all_quer/', views.trends_my_all_querPost, name='trends_my_all_quer'),
    path('trends_other_all_quer/', views.trends_other_all_querPost, name='trends_other_all_quer'),
]
