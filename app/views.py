import os

from django.core.handlers.wsgi import WSGIRequest
from django.core.mail import send_mail
from django.db.models import Q
from django.http import BadHeaderError, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_GET, require_POST

from app.forms import ContactForm
from app.models import Book, Author
from app.utils import replace_chars_in_query, create_paginator


@require_GET
def index(request: WSGIRequest):
    new_books_list = Book.get_new_books()
    context = {"new_books_list": new_books_list}
    return render(request, "app/index.html", context)


@require_GET
def get_book(request: WSGIRequest, slug: str):
    book = get_object_or_404(Book, slug=slug)
    if not request.session.get(str(book.id), False):
        book.increment_view_count()
    request.session[str(book.id)] = True

    context = {"book": book}
    return render(request, "app/book.html", context)


@require_GET
def search(request: WSGIRequest):
    if query := request.GET.get("q"):
        query = replace_chars_in_query(query)
        results = Book.objects.filter(
            Q(title__icontains=query) | Q(authors__name__icontains=query)
        ).distinct()

        context = {
            "q": query,
            "results": results,
        }
        return render(request, "app/results.html", context)
    else:
        new_books_list = Book.get_new_books()
        context = {"new_books_list": new_books_list}
        return render(request, "app/index.html", context)


@require_GET
def get_all_books(request: WSGIRequest):
    books_list = Book.objects.all()
    page_obj = create_paginator(books_list, request)
    context = {"books_list": books_list, "page_obj": page_obj}
    return render(request, "app/books.html", context)


@require_GET
def get_all_authors(request: WSGIRequest):
    authors_list = Author.objects.all()
    page_obj = create_paginator(authors_list, request)
    context = {"authors_list": authors_list, "page_obj": page_obj}
    return render(request, "app/authors.html", context)


@require_GET
def get_author(request: WSGIRequest, slug: str):
    author = get_object_or_404(Author, slug=slug)
    books_list = author.books.all()
    page_obj = create_paginator(books_list, request)
    context = {"author": author, "page_obj": page_obj}
    return render(request, "app/author.html", context)


@require_POST
def feedback(request):
    form = ContactForm(request.POST)
    if form.is_valid():
        name = form.cleaned_data["name"]
        email = form.cleaned_data["email"]
        message = form.cleaned_data["message"]
        try:
            send_mail(
                name, email + "\n" + message, email, [os.getenv("EMAIL_HOST_USER")]
            )
        except BadHeaderError:
            return HttpResponse("Invalid header found.")
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
