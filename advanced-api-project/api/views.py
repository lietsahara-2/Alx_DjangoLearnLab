from django.shortcuts import render
from rest_framework import generics, filters #for generic class-based views & filtering

from django_filters.rest_framework import DjangoFilterBackend


from .models import Book
from .models import Author
from .serializers import BookSerializer, AuthorSerializer

#from django.views.generic.list import ListView
#from django.views.generic.detail import DetailView
#from django.views.generic.edit import CreateView, UpdateView, DeleteView #for website type views..??

#from django.urls import reverse_lazy #to avoid hardcoding urls

# Create your views here.
'''removed templates and success_url comments as we are using DRF and not rendering templates'''
'''used DRF serializers for data representation instead of templates'''

"""used ListAPView,... DestroyAPIView instead of ListView,... DeleteView from django.views.generic as we are building an API using DRF"""
class BookListAPIView(generics.ListAPIView): #A ListView for retrieving all books.
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    #model = Book
    #template_name = "api/book_list.html"
    #context_object_name = "books"
    filter_backend = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]#including searching and ordering capabilities
    filterset_fields = ["title", "author", "publication_year"]
    search_fields = ["title", "author__name", "publication_year"]#__tell django to look into related model field(since author is a foreign key)
    ordering_fields = ["title", "publication_year"]


class BookDetailAPIView(generics.RetrieveAPIView): #A DetailView for retrieving a single book by ID.
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    #model = Book
    #template_name = "api/book_detail.html"
    #context_object_name = "book" #by default, DetailView uses 'object' as context name, we change it to 'book' for clarity
    


class BookCreateAPIView(generics.CreateAPIView):#A CreateView for adding a new book.
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    #model = Book
    #template_name ="api/book_form.html"
    #fields = "__all__"
    #success_url = reverse_lazy("book-list")#redirect to book list after successful creation
    

class BookUpdateAPIView(generics.UpdateAPIView): #An UpdateView for modifying an existing book.
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    #model = Book
    #template_name = "api/book_form.html"
    #fields = "__all__"
    #success_url = reverse_lazy("book-list")
    

class BookDeleteAPIView(generics.DestroyAPIView): #A DeleteView for removing a book.
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    #model = Book
    #template_name = "api/book_confirm_delete.html"
    #success_url = reverse_lazy ("book-list") # success_url = "/api/books/" --> GPT informed me its bad practice to hardcode urls
    
    #DetailView and ListView don't need success_url as they are for retrieval only

    






