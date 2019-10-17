from django.shortcuts import render
from django.shortcuts import get_object_or_404
from NibblesBookApp import models
from django.db.models import Q
from rest_framework.decorators import api_view
from rest_framework.response import Response
from NibblesBookApp import serializers
from rest_framework import status

''' generate the number of loops '''
def generate_number_of_loops(num):
    if num % 5 == 0:
        return num // 5

    return int(num // 5) + 1

''' return a list of books in chunks by a certain number '''
def return_books_by_number(queryset, number):
    book_in_number = []
    start = 0
    end = number
    loops = generate_number_of_loops(len(queryset))

    for i in range(loops):
        book_in_number.append(queryset[start:end])
        start += number
        end += number
    return book_in_number


def index(request):
    queryset = models.Book.objects.all()
    book_in_sixes = return_books_by_number(queryset, 6)
    context = {'book_in_sixes': book_in_sixes}
    return render(request, 'index.html', context)


def get_book(request, book_id):
    rating_range = range(1, 6)
    book = get_object_or_404(models.Book, id=book_id)
    book_formats = book.format_set.all()
    book_reviews = book.review_set.all()
    recommended_books = models.Book.objects.filter(Q(genre__iexact=book.genre) and ~Q(id=book.id))[:5]

    context = {'book': book,
               'book_formats': book_formats,
               'book_reviews': book_reviews,
               'recommended_books': recommended_books,
               'rating_range': rating_range,'avg': book.get_avg_rating(book_id)}

    return render(request, 'book.html', context)


def get_author(request, author_id):
    queryset = get_object_or_404(models.Author, id=author_id)
    author_books = queryset.book_set.all()
    book_in_fives_by_author = return_books_by_number(author_books, 5)
    context = {'queryset': queryset,
               'book_in_fives_by_author': book_in_fives_by_author}

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




######################### Rest functions #############################


@api_view(['GET', 'POST'])
def book_list(request):
    if request.method == 'GET':
        queryset = models.Book.objects.all()
        serialize = serializers.BookSerializer(queryset, many=True)
        return Response(serialize.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def author_list(request):
    if request.method == 'GET':
        queryset = models.Author.objects.all()
        serialize = serializers.AuthorSerializer(queryset, many=True)
        return Response(serialize.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


