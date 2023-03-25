from django.urls import path

from app import views

app_name = 'books'
urlpatterns = [
    path('', views.get_all_books, name='index'),
    path('books/<slug:slug>/', views.get_book, name='Get book'),
    path('authors/<slug:slug>', views.get_author, name='Get author'),
    path('authors/', views.get_all_authors, name='Get all authors')
]
