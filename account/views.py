from django.shortcuts import render

# Create your views here.
from django.contrib.auth import authenticate, login

from django.shortcuts import render,redirect
from chat.models import Customers,UserProfile,Message
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from chat.serializers import MessageSeriallizer
from .register import RegisterUser
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.views.decorators.debug import sensitive_post_parameters
from django.contrib.auth.models import User

def social_view(request):
    return render(request,'project/post/home.html')

def dashboard(request):
    if User.is_authenticated:
        return render(request,'chat/dashboard.html')
    else:
        return redirect("register/")        
    
@sensitive_post_parameters('pswd', 'cpswd')
def user_register(request):
    message=[]
    if request.method == 'POST':
        body = request.POST

        name=body.get('name')
        username=body.get('username')
        email=body.get('email')
        password=body.get('pswd')
        confirm_password=body.get('cpswd')

        fields = RegisterUser(name=name, username=username, email=email, password=password, confirm_password=confirm_password)
        email = fields.validate_email()
        username = fields.validate_username()
        password = fields.validate_password()
        if not email:
            message.append("Email already registered!")
        elif not username:
            message.append("Username already registered!")
        elif not password:
            message.append("Passwords don't match!")
        else:
            print("SUCCESS!!!!")
            fields.save()
            user = authenticate(username=username, password=password)
            login(request, user)
            profile = UserProfile(email=email, name=name, username=username)
            profile.save()
            return redirect("dashboard/")
        # if fields.is_valid():
        #     if password == confirm_password:
        #         fields.save()
        #         messages.info(request, 'Registeration successful')
        #         return redirect('register.html')
        # else:
        #     messages.info(request, 'confirm password and password must be the same')
        #     return redirect('register.html')

    return render(request, 'project/post/register.html', {"message": message})

def user_login(request):
    return render(request, 'project/post/login.html')
    # if request.method == 'POST':
    #     body = request.POST

    #     username = body['name']
    #     password = body['pswd']

    #     users = RegisterUser.object.get()
    #     if (username is not None and password is not None):
    #         user = authenticate(username=username, password=password)
    #         if user is not None:
