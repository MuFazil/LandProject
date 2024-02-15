from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages


# Create your views here.
def register(request):
    if(request.method=="POST"):
        u = request.POST['u']
        p = request.POST['p']
        p1 = request.POST['p1']
        e = request.POST['e']
        f = request.POST['f']
        l = request.POST['l']
        if(p==p1):
            u=User.objects.create_user(username=u,password=p,email=e,first_name=f,last_name=l)
            u.save()

            return redirect('UserAuthentication:login')  #appname:view

    return render(request,'userAuth/register.html')



def user_login(request):
    if (request.method == "POST"):
        u = (request.POST['u'])
        p = (request.POST['p'])
        user = authenticate(username=u, password=p)

        if user:
            login(request,user)
            return redirect('Home:landing')
        else:
            messages.error(request, "invalid credentials")
    return render(request,'userAuth/login.html')


def forgot_password(request):
    return render(request,'userAuth/forgot_password.html')


def reset_password(request):
    return render(request,'userAuth/reset_password.html')


def user_logout(request):
    logout(request)
    return user_login(request)