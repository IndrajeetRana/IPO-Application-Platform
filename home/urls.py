from home import views
from django.contrib import admin
from django.urls import path

app_name = 'home'

urlpatterns = [
    path('', views.home, name='home'),
    path('signin/', views.signIn, name='signin'),
    path('signup/', views.signUp, name='signup'),
    path('forgetpassword/', views.forgetPassword, name='forgetPassword'),
    path('reset-password/<uidb64>/<token>/', views.resetPassword, name='resetPassword'),
]
