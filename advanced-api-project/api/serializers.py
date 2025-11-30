from .models import Author, Book
from rest_framework import serializers
import datetime


class BookSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all())
    class Meta:
        model = Book
        fields = "__all__"
    
    #custom serializer to validate publication year
    def validate_publication_year(self, value):
        current_year = datetime.date.today().year
        if value > current_year:
            raise serializers.ValidationError("publication year can't be greater than current year")
        return value
    

#put it after books for the nesting
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True) #nested the book serializer to allow the authors books to be produced too

    class Meta:
        model = Author
        fields = ['name', 'books']#added books in the fields so that it'll show


