from django.shortcuts import render
from .models import Book, Library
from django.views.generic import DetailView

# Function-based view – list all books
def list_books(request):
    books = Book.objects.all()  # get all books from DB
    return render(request, "relationship_app/list_books.html", {"books": books})

# Class-based view – detail of a library
class LibraryDetailView(DetailView):
    model = Library
    template_name = "library_detail.html"
    context_object_name = "library"
