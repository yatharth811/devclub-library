from django.contrib import admin
from django.urls import path, include
from home import views
from home.views import booklist
urlpatterns = [
    path('', views.dashboard, name='index'),
    path('dashboard/',views.dashboard, name='dashboard'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('oauth/', include("social_django.urls")),
    path('register/', views.register, name='register'),
    path('addbook/', views.addbook, name='addbook'),
    path('books/', booklist.as_view(), name='booklist'),
    path('books/<int:id>/', views.bookspec, name='bookspecific'),
    path('searchbooks/', views.searchbooks, name='searchbooks'),
    path('bookissue/', views.issue_requests, name='issue_books'),
    path("bookissue/reject/<int:id>/", views.reject_request, name='reject_request'),
    path("bookissue/accept/<int:id>/", views.accept_request, name='accept_request'),
    path("bookissue/return/<int:id>/", views.return_request, name='return_request'),
    path("bookissue/request/<int:id>/", views.request_book, name='request_book'),
    path("editbook/<int:id>/", views.edit_book, name="editbook")
]
