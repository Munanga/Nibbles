from django.test import TestCase
from django.urls import reverse
from django.urls import resolve
from django.test import tag
from NibblesBookApp import models

@tag('all')
class AllTests(TestCase):
    def setUp(self):
        self.author = models.Author.objects.create(image='static/images/authors/Amy-Newmark.jpg',
                                                  first_name='Amy',
                                                  last_name='Newmark',
                                                  about='Good Author')

    ###################### index page view tests #######################

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

    ############################ author page view tests #################################

    @tag('author')
    def test_author_view_status_code(self):
        response = self.client.get('/nibbles/author/{0}'.format(self.author.id))
        self.assertEquals(response.status_code, 200)

    @tag('author')
    def test_author_view_url_by_name(self):
        author_url = reverse('NibblesBookApp:get_author', kwargs={'author_id':self.author.id})
        response = self.client.get(author_url)
        self.assertEquals(response.status_code, 200)

    @tag('author')
    def test_author_name_equal_index_url(self):
        resolver = resolve('/nibbles/author/1')
        view_name = 'NibblesBookApp:get_author'
        self.assertEquals(resolver.view_name, view_name)

    @tag('author')
    def test_author_view_uses_correct_template(self):
        url = reverse('NibblesBookApp:get_author', kwargs={'author_id':self.author.id})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'author.html')

    ################################### Book page view tests ################################
    # genres page view tests
    # about page view tests
