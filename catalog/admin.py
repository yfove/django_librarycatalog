from django.contrib import admin

# Register your models here.
# code below imports the models then calls admin.site.register to register each of them
from .models import Author, Genre, Book, BookInstance

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(BookInstance)