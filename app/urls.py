from django.urls import path

from app import views

app_name = 'books'
urlpatterns = [
    path('', views.get_all_books, name='index'),
    path('books/<slug:slug>/', views.get_book, name='Get book'),
]
