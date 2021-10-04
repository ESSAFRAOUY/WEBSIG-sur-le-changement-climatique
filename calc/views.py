from django.http.response import HttpResponse
from django.shortcuts import render


# Create your views here.


def home(request):
    return  render(request,'home.html')


def afficher(request):

    firstname=request.POST['fname']
    lastname=request.POST['lname']
    return render(request,'result.html',{'fname1':firstname,'lname1':lastname})