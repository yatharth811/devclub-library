from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.urls import reverse
from home.forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Book, Profile, BookRequest
from django.http import Http404, JsonResponse
from django.views.generic import ListView
from django.db.models import Q
from django.conf import settings
from django.core.mail import send_mail
# from django.views import generic

#Create your views here

def dashboard(request):
    return render(request, 'dashboard.html')

def register(request):
    if request.method == "GET":
        return render(
            request, "register.html",
            {"form": CustomUserCreationForm}
        )
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.backend = "django.contrib.auth.backends.ModelBackend"
            user.save()
            login(request, user)
            logout(request)
            subject = "Welcome to Library"
            message = f"Hi, {user.username},\nThank you for registering!"
            email_from=settings.EMAIL_HOST_USER
            recipient_list = [user.email]
            send_mail(subject, message, email_from, recipient_list)

            return redirect(reverse("dashboard"))
        else:
            return render(request, 'register.html', {"form": CustomUserCreationForm})
@login_required(login_url='/accounts/login/')
def addbook(request):
    if request.method=='POST':
        title = request.POST.get("book_title")
        author = request.POST.get("book_author")
        publisher = request.POST.get("book_publisher")
        genre = request.POST.get("book_genre")
        summary = request.POST.get("book_summary")
        isbn = request.POST.get("book_isbn")
        is_available = request.POST.get("book_availability")

        if (is_available=="True"):
            is_available=True
        else:
            is_available=False
        img = request.POST.get("book_img")
        newbook = Book(title = title, author=author,publisher=publisher, genre=genre, summary=summary, isbn=isbn, img = img, is_available=is_available)
        newbook.save()

    return render(request, 'addbook.html')


class booklist(ListView):
    model = Book



def bookspec(request,id):
    bookitem = Book.objects.get(id=id)
    return render(request, 'home/book.html', {'bookitem':bookitem})



def searchbooks(request):
    if request.method == 'GET':
        query= request.GET.get('q')

        submitbutton= request.GET.get('submit')

        if query is not None:
            lookups= Q(title__icontains=query) | Q(title__icontains=query)

            results= Book.objects.filter(lookups).distinct()

            context={'results': results,
                     'submitbutton': submitbutton}

            return render(request, 'search.html', context)

        else:
            return render(request, 'search.html')

    else:
        return render(request, 'search.html')

@login_required(login_url='/accounts/login/')
def issue_requests(request):
    book_requests = BookRequest.objects.filter(status='PEN')
    accepted = BookRequest.objects.filter(status='ACC')
    context = {
        "book_requests" : book_requests,
        "accepted" : accepted
    }

    return render(request, 'book_issue.html', context)

@login_required(login_url='/accounts/login/')
def reject_request(request, id):
    book_requests = BookRequest.objects.filter(status='PEN')
    accepted = BookRequest.objects.filter(status='ACC')
    context = {
        "book_requests" : book_requests,
        "accepted" : accepted
    }
    reject_list = BookRequest.objects.get(id=id)
    reject_list.status = "REJ"
    reject_list.delete()
    return render(request, 'book_issue.html', context)

@login_required(login_url='/accounts/login/')
def accept_request(request, id):
    book_requests = BookRequest.objects.filter(status='PEN')
    accepted = BookRequest.objects.filter(status='ACC')
    context = {
        "book_requests" : book_requests,
        "accepted" : accepted
    }
    accept_list = BookRequest.objects.get(id=id)
    accept_list.status = "ACC"
    accept_list.save(update_fields=['status'])
    return render(request, 'book_issue.html', context)

@login_required(login_url='/accounts/login/')
def return_request(request, id):
    book_requests = BookRequest.objects.filter(status='PEN')
    accepted = BookRequest.objects.filter(status='ACC')
    context = {
        "book_requests" : book_requests,
        "accepted" : accepted
    }

    return_list = BookRequest.objects.get(id=id)
    return_list.delete()
    return render(request, 'book_issue.html', context)

@login_required(login_url='/accounts/login/')
def request_book(request, id):
    req_book = Book.objects.get(id=id)
    requested_by = Profile.objects.get(user=request.user)
    request_date = datetime.today()

    bookrequest = BookRequest(book=req_book, requested_by=requested_by, request_date=request_date)
    bookrequest.save()

    return redirect(reverse("dashboard"))

@login_required(login_url='/accounts/login/')
def edit_book(request, id):
    edit = Book.objects.get(id=id)
    if request.method=='POST':
        edit.title = request.POST.get("book_title")
        edit.author = request.POST.get("book_author")
        edit.publisher = request.POST.get("book_publisher")
        edit.genre = request.POST.get("book_genre")
        edit.summary = request.POST.get("book_summary")
        edit.isbn = request.POST.get("book_isbn")
        is_available = request.POST.get("book_availability")

        if (is_available=="True"):
            edit.is_available=True
        else:
            edit.is_available=False
        edit.img = request.POST.get("book_img")
        edit.save(update_fields=["title","author","publisher","genre","summary","isbn","is_available","img"])

    return render(request, 'editbook.html')