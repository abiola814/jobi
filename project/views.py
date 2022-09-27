# from ssl import _PasswordType
from contextlib import redirect_stderr
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .register import RegisterUser
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.views.decorators.debug import sensitive_post_parameters

# Create your views here.

def social_view(request):
    return render(request,'project/post/home.html')

@sensitive_post_parameters('pswd', 'cpswd')
def user_register(request):
    if request.method == 'POST':
        body = request.POST

        name=body['name']
        username=body['username']
        email=body['email']
        password=body['pswd']
        confirm_password=body['cpswd']

        if name is not None and username is not None and email is not None and password is not None and confirm_password is not None:
            if confirm_password == password:
                fields = RegisterUser()
                fields.name = name
                fields.username = username
                fields.email = email
                fields.password = password
                fields.confirm_password = confirm_password
                fields.save()
                messages.info(request, 'Registeration successful')
                return redirect('register.html')
            else:
                messages.info(request, 'confirm password and password must be the same')
                return redirect('register.html')

        else:
            messages.info(request, 'All fields must not be empty')
            return redirect('register.html')
    else:
        return render(request, 'register.html')
        
