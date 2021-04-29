
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.db.models.signals import post_save
from datetime import datetime
from django.dispatch import receiver


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=250,default="")
    publisher = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    summary = models.TextField(max_length=2000)
    isbn = models.CharField(max_length=13)
    is_available = models.BooleanField(default=False)
    img = models.URLField(default="https://dynamicmediainstitute.org/wp-content/themes/dynamic-media-institute/imagery/default-book.png", max_length=2000,help_text="Enter url for the image")
    def __str__(self):
        return self.title
    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=200, default='Computer Science')
    is_librarian = models.BooleanField(default=False)
    is_student = models.BooleanField(default=True)
    def __str__(self):
        return self.user.username

class BookRequest(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    requested_by = models.ForeignKey(Profile, on_delete=models.CASCADE)
    request_date = models.DateTimeField(default=datetime.now)
    # response = models.BooleanField(default=False)
    choices = (
        ('ACC','Accept'),
        ('REJ','Reject'),
        ('PEN','Pending'),
    )
    # issue_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=3, choices=choices, default='PEN', help_text='Issue Status')
    def __str__(self):
        return "{}---{}---{}".format(self.book,self.requested_by, self.request_date)

    

# class BookIssue(models.Model):
#     bookrequest = models.OneToOneField(BookRequest, on_delete=models.CASCADE)
#     issued_to = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)

#     def __str__(self):
#         return self.bookrequest.book.title
    
    # def give_book(self):
    #     book = models.ForeignKey()
    #     if (book.num_available>0):
    #         book.num_available-=1
    #     book.save()


# class BookReturn(models.Model):
#     bookrequest = models.OneToOneField(BookRequest.status, on_delete=models.CASCADE, )
#     returned_by = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
#     return_date = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.bookrequest.book.title

#     def add_book(self):
#         book = models.ForeignKey(Book, on_delete=models.CASCADE)
#         book.num_available+=1
#         book.save()
