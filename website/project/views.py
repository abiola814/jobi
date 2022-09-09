from django.shortcuts import render
from django.http import HttpResponse
from .login import LoginForm
from django.contrib.auth import authenticate, login

# Create your views here.

def social_view(request):
    return render(request,'project/post/home.html')

def login(request):
    return render(request, 'project/post/login.html')

def user_register(request):
    return render(request, 'project/post/register.html')
        
