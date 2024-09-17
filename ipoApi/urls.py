# ipo_data/urls.py

from django.urls import path
from .views import IPOListCreateView, IPODetailView
from django.shortcuts import render

urlpatterns = [
    path('ipos/', IPOListCreateView.as_view(), name='ipo-list-create'),
    path('ipos/<int:pk>/', IPODetailView.as_view(), name='ipo-detail'),
    path('create-ipo/', lambda request: render(request, 'ipo_data/ipo_form.html'), name='create-ipo'),
]
