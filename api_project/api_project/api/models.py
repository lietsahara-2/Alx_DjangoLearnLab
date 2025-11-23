from django.db import models


# Create your models here.
class Book(models.Model):
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=200)

#adding authentication to models
#automatic/ when admin adds
#should be in models.py or signals.py
'''
from django.db.models.sgnals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
'''




#manual/ when user is created (logs in on their own) Gpt recommended
#shouldbe in views.py
'''

from rest_framework.views import APIView
from rest_framework.authtoken.models import Token

class LoginView(APIView):
    def post(self, request):
        #Token generated only if user logs in successfully
        token, created = Token.objects.get_or_create(user=user)
'''


#manual with error message
'''
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication

class LoginView(APIView):
    authentication_classes = [TokenAuthentication]

    def post(self, request):
        # authentication logic 
        user = authenticate(username=request.data['username'], password=request.data['password'])
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        else:
            return Response({'error': 'Invalid credentials'}, status=401)
'''