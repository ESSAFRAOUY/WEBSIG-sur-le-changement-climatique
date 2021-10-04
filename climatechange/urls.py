from os import name
from django.urls import path
from django.urls import URLPattern
from . import views
from django.contrib.auth import views as auth_views

urlpatterns=[
    #path('login/',views.login,name='login'),
   # path('register/',views.register,name='register'),
    path('documents/',views.documents,name='documents'),
    path('',views.index,name='index'),
    path('charts/',views.charts,name='charts'),
    path('acteurs/',views.actors,name='actors'),
    path('actions/',views.actions,name='actions'),



   
]