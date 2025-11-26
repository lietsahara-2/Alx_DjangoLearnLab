from django.db import models
#for custom user
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext_lazy as _ #to enable translation if it might become multilingual (not a must)
#
from django.conf import settings # to refer to AUTH_USER_MODEL --> added_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)

# Create your models here.
#1.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True) #ili ujue mwenye ameongeza kitabu

#++ Managing custom user model
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError(_("Email address required"))#this can thus be translated later
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_("Superuser must have is_staff=True"))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True'))
        return self.create_user(email, password, **extra_fields)


#++ creating custom user
class CustomUser(AbstractUser):
    username = None  #removing username field coz we will use email instead
    email = models.EmailField(unique=True)

    #added as per the project requirement
    date_of_birth = models.DateField()
    profile_photo = models.ImageField(upload_to = "profile_pictures/", null = True, blank = True) 

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

#permissions added
    class Meta:
        permissions = [
            ("can_view", "Can view books"),
            ("can_create", "Can create books"),
            ("can_edit", "Can edit books"),
            ("can_delete", "Can delete books"),
        ]

    def __str__(self):
        return self.title