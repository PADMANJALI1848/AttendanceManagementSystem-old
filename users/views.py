from django.shortcuts import render , redirect
from django.http import HttpResponse

# Create your views here.
def home_view(request ,*args , **kwargs):
    print(args,kwargs)
    print(request.user)
    return render(request , "home.html",{})

def SignUp_view(request):
    return render(request, 'Signup.html', {})