from django.contrib import admin
from .models import Book, Profile, BookRequest

# Register your models here.
admin.site.register(Book)
admin.site.register(Profile)
# admin.site.register(BookIssue)
admin.site.register(BookRequest)
