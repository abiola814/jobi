from django.urls import path
from . import views

app_name = 'project'

urlpatterns=[
    path('', views.social_view, name='social_view'),
    path('login/', views.login, name='login'),
    path('', views.user_register, name='user_register'),
]