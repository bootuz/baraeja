from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_GET

from app.models import Book, Author


@require_GET
def get_all_books(request):
    books = Book.objects.all()
    return HttpResponse(books)


@require_GET
def get_book(request, slug: str):
    book = get_object_or_404(Book, slug=slug)
    if not request.session.get(str(book.id), False):
        book.increment_view_count()
    request.session[str(book.id)] = True
    return HttpResponse(book)


@require_GET
def get_all_authors(request):
    authors = Author.objects.all()
    print(type(request))
    return HttpResponse(authors)


@require_GET
def get_author(request, slug: str):
    author = get_object_or_404(Author, slug=slug)
    return HttpResponse(author)
