from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from django.http.response import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.




def login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Invalid credentials')
            return redirect('/accounts/login')


    else:
        return render(request,'login.html')




def register(request):

    if request.method == 'POST':
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1==password2 :
            if User.objects.filter(username=username).exists():
                messages.info(request,'username is taken')
                #return render (request,'/accounts/register',{'messages1':messages1})
                return redirect('/accounts/register')
                
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email already exists')
                return redirect('/accounts/register')
            else:
                user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password1)
                user.save()
                print('user created')
                return redirect('/accounts/login')

        else :
            messages.info(request,'passwords not matching...')
            return redirect('/accounts/login')
        #return redirect('/accounts/login')

    else:
        return render(request,'register.html')



def password(request):
    return render(request,'password_reset.html')


def logout(request):
    auth.logout(request)
    return redirect('/')



