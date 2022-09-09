from django.contrib import admin

# Register your models here.from django.contrib import admin
from .models import Userprofile, Message, Customers

# Register your models here.
admin.site.register(Userprofile)
admin.site.register(Message)
admin.site.register(Customers)
