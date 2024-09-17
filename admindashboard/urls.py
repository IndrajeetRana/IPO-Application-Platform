from django.urls import path

from .import views

app_name = 'admindashboard'

urlpatterns = [
    path('', views.adminPage, name='adminPage'),
    path('manageipo/' ,views.manageIpo,name='manageIpo'),
    path('register/', views.register, name='registerIpo'),
    
]