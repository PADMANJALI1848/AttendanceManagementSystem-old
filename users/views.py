from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login

# Create your views here.
def home(request ,*args , **kwargs):
    print(args,kwargs)
    return render(request , "home.html",{})

def signUp(request):
    return render(request,'SignUp.html', {})

def facultyCourses(request):
    return render(request , 'facultyCourses.html')

def facultySections(request):
    return render(request , 'facultySections.html')

def facultyAttendance(request):
    return render(request,'facultyAttendance.html')