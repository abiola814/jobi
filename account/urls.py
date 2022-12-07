from django.urls import path,re_path
from . import views
from django.contrib.auth import views as auth_views


app_name = 'project'

urlpatterns=[
    path('', views.social_view, name='social_view'),
    path('register/', views.user_register, name='user_register'),
    path('register/user_register', views.user_register, name='user_register'),
    path('login/', views.user_login, name='user_login'),
    path('register/dashboard/', views.dashboard, name='dashboard'),
]
