from os import name
from django.urls import path
from django.urls import URLPattern
from . import views


urlpatterns=[
    path('',views.home,name='home'),
    path('afficher',views.afficher,name='afficher')
]