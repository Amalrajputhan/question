from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User

from .forms import LocationForm
from .models import Courses



from django.contrib import messages, auth
from django.contrib.auth.models import User
from django import forms
from django.http import HttpResponse
from django.shortcuts import render, redirect
# from .forms import STOREModelform
from django import forms
from django.shortcuts import render


def amal(request):
    return render(request,"amal.html")
def register (request):
    if request.method=="POST":
        username=request.POST['username']
        # first_name = request.POST['first_name']
        # last_name=request.POST['last_name']
        # email=request.POST['email']
        password=request.POST['password']
        cpassword=request.POST['password1']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"user name Taken")
                return redirect('register')
            # elif User.objects.filter(email=email).exists():
            #     messages.info(request, "email already taken")
            #     return redirect('register')
            else:

                user=User.objects.create_user(username=username,password=password)
                # first_name = first_name, last_name = last_name, email = email
                user.save();
                return redirect('login')

        else:
            messages.info(request, "password not matching")
            return redirect('register')
        return redirect('login')
    return  render(request,"register.html")
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            # return redirect('/')
            # return redirect('')
            return render(request, "welcome.html")
        else:
            messages.info(request,"invalid credentials")
            return  redirect('login')
    return  render(request,"login.html")

def logout(request):
    auth.logout(request)
    return redirect('/')
# def prof(request):
#   return render(request,"welcome.html")

def Home(request):
    return redirect('/')
def index(request):
    if request.method == "POST":
        form = LocationForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data["department"])
            print(form.cleaned_data["courses"])
            message = 'Order confirmed'
            return render(request, 'success_page.html', {'message': message})
        else:
            print(form.errors)
    else:
        form = LocationForm()
    return render(request, 'index.html', {"form": form})

def load_courses(request):
    department_id = request.GET.get("department")
    courses = Courses.objects.filter(department_id=department_id)
    return render(request, "courses_options.html", {"courses":courses})



