from django.shortcuts import render , redirect
from django.http import HttpResponse

# Create your views here.
def home(request ,*args , **kwargs):
    print(args,kwargs)
    print(request.user)
    return render(request , "home.html",{})

def SignUp(request):
    return render(request, 'Signup.html', {})

def Login(request):
    return render(request, 'login.html', {})

def StudentDashboard(request):
    return render(request, 'studentdashboard.html', {})

def StudentCourse(request):
    return render(request, 'studentcourse.html', {})