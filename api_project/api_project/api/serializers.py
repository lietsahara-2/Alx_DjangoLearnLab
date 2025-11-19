from rest_framework import serializers
from .models import Book                            #importing the model to be serialised from the models file

class BookSerializer(serializers.ModelSerializer):    #defining the serializer class
    class Meta:                                     #configures what to serialize
        model = Book
        fields = "__all__"