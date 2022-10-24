from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class Book(models.Model):
    book_id = models.CharField(max_length=12)
    etag = models.CharField(max_length=11)
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author, related_name='authors')
    published_date = models.CharField(max_length=10)
    categories = models.TextField(null=True)
    average_rating = models.IntegerField(null=True)
    ratings_count = models.IntegerField(null=True)
    thumbnail = models.CharField(null=True, max_length=100)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title
