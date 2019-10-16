from django.shortcuts import render
from django.shortcuts import get_object_or_404
from NibblesBookApp import models
from django.db.models import Q


''' generate the number of loops '''
def generate_number_of_loops(num):
    if num % 5 == 0:
        return num / 5

    return int(num / 5) + 1


def index(request):
    queryset = models.Book.objects.all()
    book_in_fives = []
    start = 0
    end = 6
    loops = generate_number_of_loops(len(queryset))

    for i in range(loops):
        book_in_fives.append(queryset[start:end])
        start += 6
        end += 6

    print(book_in_fives)
    context = {'book_in_fives': book_in_fives}
    return render(request, 'index.html', context)


def get_book(request, book_id):
    book = get_object_or_404(models.Book, id=book_id)
    book_formats = book.format_set.all()
    book_reviews = book.review_set.all()
    recommended_books = models.Book.objects.filter(Q(genre__iexact=book.genre) and ~Q(id=book.id))[:5]

    context = {'book': book,
               'book_formats': book_formats,
               'book_reviews': book_reviews,
               'recommended_books': recommended_books}

    return render(request, 'book.html', context)


def get_author(request, author_id):
    queryset = get_object_or_404(models.Author, id=author_id)
    books_by_author = queryset.book_set.all()

    context = {'queryset': queryset,
               'books_by_author': books_by_author}

    return render(request, 'author.html', context)


def get_genre(request, genre):
    queryset = models.Book.objects.filter(genre=genre)
    context = {'queryset': queryset, 'genre': genre}
    return render(request, 'genres.html', context)


def search(request):
    query = request.GET.get('query')
    queryset = []
    exists = False

    if request.method == 'GET':
        if query:
            queryset = models.Book.objects.filter(Q(title__iexact=query) |
                                              Q(title__icontains=query))
            exists = queryset.exists()

    context = {'queryset': queryset, 'exists': exists, 'query': query}
    return render(request, 'search.html', context)


def about(request):
    template = 'about.html'
    return render(request, template)


def contact(request):
    pass



