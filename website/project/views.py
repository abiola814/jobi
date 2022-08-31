from django.shortcuts import render

# Create your views here.

def social_view(request):
    return render(request,'project/post/home.html')
