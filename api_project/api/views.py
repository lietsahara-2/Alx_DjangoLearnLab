from django.shortcuts import render
from rest_framework import generics
#from rest_framework.generics import GenericAPIView
from .models import Book                                            #will be used for query
from .serializers import BookSerializer #LoginSerializer            #for serialization
#expanding functionality using DRF
from rest_framework import viewsets

from rest_framework.permissions import IsAuthenticated

# a.) Create your views here.
#1. Basic API can only GET or POST
class BookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer           #use BookSerializer for serializing data

 #2. Full CRUD API with all operations 
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    permission_classes = [IsAuthenticated]  #only authenticated users can access


#b.) Creating a login view for token generation
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate    

class LoginView(APIView): #natoa za serializer na (GenericAPIView) for now to simplify

    #serializer_class = LoginSerializer 
    
    def post(self, request):

       # serializer = LoginSerializer(data=request.data)
       # serializer.is_valid(raise_exception=True)
    
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        
   
    #handling missing username or password
    '''
     if not username or not password:
        return Response(
        {'error': 'Username and password required.'},
        status=status.HTTP_400_BAD_REQUEST
    )
    '''
