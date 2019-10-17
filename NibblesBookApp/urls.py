from django.urls import path
from NibblesBookApp import views

app_name = 'NibblesBookApp'

urlpatterns = [
    path('book/<int:book_id>', views.get_book, name='get_book'),
    path('genre/<str:genre>', views.get_genre, name='get_genre'),
    path('author/<int:author_id>', views.get_author, name='get_author'),
    path('search/', views.search, name='search'),
    path('api/books/', views.book_list, name='api_book_list'),
    path('api/author/', views.author_list, name='api_author_list'),
]