from django.db import models

# Create your models here.
class Author(models.Model):
    name=models.CharField(max_length=100)
    
class Book(models.Model):
    title=models.CharField(max_length=100)
    publication_year=models.DateField()
    # author=models.CharField(max_length=100) #we already have author just connect with foreign key
    author=models.ForeignKey(Author, on_delete=models.CASCADE)
  