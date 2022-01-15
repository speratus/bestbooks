from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=255)
    birthdate = models.DateField(auto_now=False)
    bio = models.TextField()
    tags = models.ManyToManyField('Tag', related_name='authors')
    # books = models.ManyToManyField('Book')

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    summary = models.TextField()
    review = models.TextField()
    date_published = models.DateField(auto_now=False)
    date_added = models.DateTimeField(auto_now_add=True)
    url = models.CharField(max_length=512)
    rating = models.IntegerField()
    cover_art = models.CharField(max_length=512)
    author = models.ManyToManyField('Author', related_name='books')
    tags = models.ManyToManyField('Tag', related_name='books')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='books')
    genres = models.ManyToManyField('Genre', related_name='books')

    def __str__(self):
        return self.title

