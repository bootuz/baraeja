from django.urls import path

from app import views

app_name = 'books'
urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('books/', views.get_all_books, name='get_all_books'),
    path('books/<slug:slug>/', views.get_book, name='get_book'),
    path('authors/<slug:slug>/', views.get_author, name='Get author'),
    path('authors/', views.get_all_authors, name='Get all authors')
]
