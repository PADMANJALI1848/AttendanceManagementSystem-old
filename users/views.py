from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .forms import Userform

# Create your views here.
def home(request ,*args , **kwargs):
    print(args,kwargs)
    print(request.user)
    return render(request , "home.html",{})

def SignUp(request):
    if request.method == 'POST':
        form=Userform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = Userform()
    return render(request , "SignUp.html",{ 'form': form})
	 

def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request , username=username , password=password)
        if user is not None:
            form=login(request, user)
            return redirect('studentdashboard')
        else:
            messages.info(request,f'Account Does not exit plz sign in')
    form=AuthenticationForm()
    return render(request, 'login.html', { 'form': form})


def StudentDashboard(request):
    return render(request, 'studentdashboard.html', {})

def StudentCourse(request):
    return render(request, 'studentcourse.html', {})

def facultyCourses(request):
    return render(request , 'facultyCourses.html')

def facultySections(request):
    return render(request , 'facultySections.html')

def facultyAttendance(request):
    return render(request,'facultyAttendance.html')

