from django.core.handlers.wsgi import WSGIRequest
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_GET

from app.models import Book, Author
from app.utils import replace_chars_in_query, create_paginator


@require_GET
def index(request: WSGIRequest):
    # TODO: do not forget to add this into the template
    new_books_list = Book.objects.order_by('-created_at')[:9]

    context = {
        "new_books_list": new_books_list
    }
    return render(request, 'app/index.html', context)


@require_GET
def get_book(request: WSGIRequest, slug: str):
    book = get_object_or_404(Book, slug=slug)
    if not request.session.get(str(book.id), False):
        book.increment_view_count()
    request.session[str(book.id)] = True

    context = {
        'book': book
    }
    return render(request, 'app/book.html', context)


@require_GET
def search(request: WSGIRequest):
    if query := request.GET['q']:
        query = replace_chars_in_query(query)
        results = Book.objects.filter(
            Q(title__icontains=query) | Q(authors__name__icontains=query)
        ).distinct()

        context = {
            'q': query,
            'results': results,
        }
        return render(request, 'app/results.html', context)
    else:
        return render(request, 'app/index.html')


@require_GET
def get_all_books(request: WSGIRequest):
    books_list = Book.objects.all()
    page_obj = create_paginator(books_list, request)
    context = {
        "books_list": books_list,
        "page_obj": page_obj
    }
    return render(request, 'app/books.html', context)


@require_GET
def get_all_authors(request: WSGIRequest):
    authors_list = Author.objects.all()
    page_obj = create_paginator(authors_list, request)
    context = {
        "authors_list": authors_list,
        "page_obj": page_obj
    }
    return render(request, 'app/authors.html', context)


@require_GET
def get_author(request: WSGIRequest, slug: str):
    author = get_object_or_404(Author, slug=slug)
    books_list = author.books.all()
    page_obj = create_paginator(books_list, request)
    context = {
        "author": author,
        "page_obj": page_obj
    }
    return render(request, 'app/author.html', context)
