from django.core.handlers.wsgi import WSGIRequest
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_GET

from app.models import Book, Author, Category
from app.utils import replace_chars


@require_GET
def index(request: WSGIRequest):
    return render(request, 'app/index.html')


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
        query = replace_chars(query)
        results = Book.objects.filter(
            Q(title__icontains=query) | Q(authors__name__icontains=query)
        ).distinct()

        context = {
            'q': query,
            'results': results,
            'count': len(results),
        }
        return render(request, 'app/results.html', context)
    else:
        return render(request, 'app/index.html')


@require_GET
def get_all_books(request: WSGIRequest):
    books = Book.objects.all()
    paginator = Paginator(books, 30)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "books": books,
        "page_obj": page_obj
    }
    return render(request, 'app/books.html', context)


@require_GET
def get_all_authors(request: WSGIRequest):
    authors = Author.objects.all()
    print(type(authors))
    return HttpResponse(authors)


@require_GET
def get_author(request: WSGIRequest, slug: str):
    author = get_object_or_404(Author, slug=slug)
    return HttpResponse(author)
