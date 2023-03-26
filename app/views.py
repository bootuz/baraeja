from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_GET

from app.models import Book, Author
from app.utils import replace_chars


@require_GET
def index(request):
    return render(request, "app/index.html")

@require_GET
def search(request):
    if 'q' in request.GET and request.GET['q']:
        query = replace_chars(request.GET['q'])
        results = Book.objects.filter(Q(title__icontains=query) | Q(authors__name__icontains=query)).distinct()

        context = {
            'q': query,
            'results': results,
            'count': len(results),
        }
        return render(request, 'app/results.html', context)
    else:
        return render(request, 'app/index.html')


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
