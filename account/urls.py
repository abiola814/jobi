from django.urls import path
from . import views

app_name = 'project'

urlpatterns=[
    path('', views.social_view, name='social_view'),
    path('register/', views.user_register, name='user_register'),
    path('register/user_register', views.user_register, name='user_register'),
    path('register/dashboard/', views.dashboard, name='dashboard'),
]
