from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.Charefield(max_length=100)

class Book(models.Moedel):
    title = models.Charfield(max_length=200)
    author = models.ForeignKey(Author)

class Library(models.Model):
    name = models.Charfield(max_length=200)
    books = models.ManyToManyField(Book)

class Librarian(models.Model):
    name = models.Charfield(max_length=100)
    library = models.OneToOneField(Library)