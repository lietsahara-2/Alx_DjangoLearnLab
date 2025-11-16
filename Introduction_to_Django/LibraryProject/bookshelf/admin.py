from django.contrib import admin

# Register your models here.
from .models import Book

#customizing the admin interface

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date')
    search_fields = ('title', 'author')
#done customizing    

admin.site.register(Book, BookAdmin)
