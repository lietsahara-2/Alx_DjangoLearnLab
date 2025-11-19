from django.shortcuts import render
from rest_framework import generics
from .models import Book                         #will be used for query
from .serializers import BookSerializer         #for serialization

# Create your views here.
class BookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer           #use BookSerializer for serializing data


