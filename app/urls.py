from django.conf.urls.static import static
from django.urls import path

from app import views
from baraeja import settings

app_name = "books"
urlpatterns = [
    path("", views.index, name="index"),
    path("search/", views.search, name="search"),
    path("books/", views.get_all_books, name="get_all_books"),
    path("authors/", views.get_all_authors, name="get_all_authors"),
    path("books/<slug:slug>/", views.get_book, name="get_book"),
    path("authors/<slug:slug>/", views.get_author, name="get_books_of_author"),
    path("feedback/", views.feedback, name="send_feedback"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
