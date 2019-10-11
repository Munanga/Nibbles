from django.urls import path
from NibblesBookApp import views

app_name = 'NibblesBookApp'

urlpatterns = [
    path('book/<int:book_id>', views.get_book, name='get_book'),
    path('genres/<str:genre>', views.get_genres, name='get_genres'),
    path('author/<int:author_id>', views.get_author, name='get_author'),
    path('search/', views.search, name='search'),
]