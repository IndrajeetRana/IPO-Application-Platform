# ipo_data/views.py

from rest_framework import generics
from rest_framework.parsers import MultiPartParser, FormParser
from .models import IPO
from .serializers import IPOSerializer

class IPOListCreateView(generics.ListCreateAPIView):
    queryset = IPO.objects.all()
    serializer_class = IPOSerializer
    parser_classes = (MultiPartParser, FormParser)  # Support file uploads

class IPODetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = IPO.objects.all()
    serializer_class = IPOSerializer
