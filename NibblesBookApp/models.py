from django.db import models
from djmoney.models.fields import MoneyField


class Author(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    image = models.CharField(max_length=50, default='static/images/authors/')
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    about = models.CharField(max_length=1000, default='None')

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    def full_name(self):
        return self.first_name + ' ' + self.last_name


class Publisher(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Store(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name


class Book(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    image = models.CharField(max_length=300, default='static/images/books/')
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    pages = models.PositiveSmallIntegerField()
    description = models.CharField(max_length=700)
    genre = models.CharField(max_length=30)
    isbn = models.BigIntegerField()
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    date = models.DateTimeField(null=True, blank=True)
    store = models.ManyToManyField(Store)

    def __str__(self):
        return self.title


class Format(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    format_type = models.CharField(max_length=40)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    price = MoneyField(max_digits=10, decimal_places=2, default_currency='USD')

    def __str__(self):
        return self.format_type


class Review(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    reviewer = models.CharField(max_length=50)
    date = models.DateTimeField(blank=True, null=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    content = models.CharField(max_length=600, default='Good read!')

    def __str__(self):
        return self.book.title




