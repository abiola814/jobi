from django.shortcuts import render
from .models import Customers,Userprofile,Message

# Create your views here.

def getcustomerlist(id):
    try:
        customer=Userprofile.objects.get(id=id)
        customerlist=list(customer.customers_set.all())
        customers =[]
        for customerid in customerlist:
            num =str(customerid)
            data= Userprofile.objects.get(id=customerid)
            customers.append(data)
        return customers
    except:
        return []

def getuserid(username):
    """
    get user id by using username
    Arg:username
    return:int
    """
    userprofile=Userprofile.objects.get(username=username)
    result =userprofile.id
    return result

def chat(request,username):
    """
    cha
    """
    pass

def index(request):
    """
    check if the user is authenticated
    for safetety reason
    """
    if not request.user.is_authenticated:
        print('not yet login')
        return render(request,'chat/signin.html')
    else:
        username=request.user.username
        id = getuserid(username)
        customerresult = getcustomerlist(id)
        print(customerresult)

        return render(request,'chat/base.html',{'customers':customerresult})




