from django.test import TestCase
from django.urls import reverse
from django.urls import resolve
from django.test import tag
from NibblesBookApp import models
from datetime import datetime
from django.utils import timezone


@tag('all')
class AllTests(TestCase):
    def setUp(self):
        self.author = models.Author.objects.create(image='static/images/authors/Amy-Newmark.jpg',
                                                  first_name='Amy',
                                                  last_name='Newmark',
                                                  about='Good Author')
        self.publisher = models.Publisher.objects.create(name="Book Publisher")
        self.store = models.Store.objects.create(name="B&N")
        self.book = models.Book.objects.create(image='static/images/books/HomeWork.jpg',
                                               title='101',
                                               author=self.author,
                                               pages=342,
                                               description='Stuff',
                                               genre='Business',
                                               isbn=9783161484100,
                                               publisher=self.publisher,
                                               date=datetime.now(tz=timezone.utc)
                                              )

        self.review = models.Review.objects.create(reviewer='Slim',
                                                   date=datetime.now(tz=timezone.utc),
                                                   book=self.book,
                                                   content="Good")
        self.format = models.Format.objects.create(format_type='Slim',
                                                   book=self.book,
                                                   price=45.5)


    ''' index page view tests '''

    @tag('index')
    def test_index_view_status_code(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

    @tag('index')
    def test_index_view_url_by_name(self):
        url = reverse('index')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    @tag('index')
    def test_index_name_equal_index_url(self):
        resolver = resolve('/')
        view_name = 'index'
        self.assertEquals(resolver.view_name, view_name)

    @tag('index')
    def test_index_view_uses_correct_template(self):
        url = reverse('index')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')





    ''' author page view tests '''

    @tag('author')
    def test_author_view_status_code(self):
        response = self.client.get('/nibbles/author/{0}'.format(self.author.id))
        self.assertEquals(response.status_code, 200)

    @tag('author')
    def test_author_view_url_by_name(self):
        author_url = reverse('NibblesBookApp:get_author', kwargs={'author_id': self.author.id})
        response = self.client.get(author_url)
        self.assertEquals(response.status_code, 200)

    @tag('author')
    def test_author_name_equal_author_url(self):
        resolver = resolve('/nibbles/author/{0}'.format(self.author.id))
        view_name = 'NibblesBookApp:get_author'
        self.assertEquals(resolver.view_name, view_name)

    @tag('author')
    def test_author_view_uses_correct_template(self):
        url = reverse('NibblesBookApp:get_author', kwargs={'author_id': self.author.id})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'author.html')




    ''' Book page view tests '''

    @tag('book')
    def test_book_view_status_code(self):
        response = self.client.get('/nibbles/book/{0}'.format(self.book.id))
        self.assertEquals(response.status_code, 200)

    @tag('book')
    def test_book_view_url_by_name(self):
        book_url = reverse('NibblesBookApp:get_book', kwargs={'book_id': self.author.id})
        response = self.client.get(book_url)
        self.assertEquals(response.status_code, 200)

    @tag('book')
    def test_book_name_equal_author_url(self):
        resolver = resolve('/nibbles/book/{0}'.format(self.book.id))
        view_name = 'NibblesBookApp:get_book'
        self.assertEquals(resolver.view_name, view_name)

    @tag('book')
    def test_book_view_uses_correct_template(self):
        url = reverse('NibblesBookApp:get_book', kwargs={'book_id': self.book.id})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'book.html')




    ''' genre page view tests '''

    @tag('genre')
    def test_genre_view_status_code(self):
        response = self.client.get('/nibbles/genre/{0}'.format(self.book.genre))
        self.assertEquals(response.status_code, 200)

    @tag('genre')
    def test_genre_view_url_by_name(self):
        genre_url = reverse('NibblesBookApp:get_genre', kwargs={'genre': self.book.genre})
        response = self.client.get(genre_url)
        self.assertEquals(response.status_code, 200)

    @tag('genre')
    def test_genre_name_equal_author_url(self):
        resolver = resolve('/nibbles/genre/{0}'.format(self.book.genre))
        view_name = 'NibblesBookApp:get_genre'
        self.assertEquals(resolver.view_name, view_name)

    @tag('a')
    def test_genre_view_uses_correct_template(self):
        url = reverse('NibblesBookApp:get_genre', kwargs={'genre': self.book.genre})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'genres.html')


    ################################### about page view tests ###############################

    @tag('about')
    def test_about_view_status_code(self):
        response = self.client.get('/about/')
        self.assertEquals(response.status_code, 200)

    @tag('about')
    def test_about_view_url_by_name(self):
        url = reverse('about')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    @tag('about')
    def test_about_name_equal_index_url(self):
        resolver = resolve('/about/')
        view_name = 'about'
        self.assertEquals(resolver.view_name, view_name)

    @tag('about')
    def test_about_view_uses_correct_template(self):
        url = reverse('about')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')
