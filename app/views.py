from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views.decorators.http import require_GET

from app.models import Book


@require_GET
def get_all_books(request):
    books = get_list_or_404(Book)
    return HttpResponse(books)


@require_GET
def get_book(request, slug: str):
    book = get_object_or_404(Book, slug=slug)
    if not request.session.get(str(book.id), False):
        book.increment_view_count()
    request.session[str(book.id)] = True
    return HttpResponse(book)
