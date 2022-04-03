from django.db import models

from django.template.defaultfilters import slugify

from autoroute.helpers import ReadView
from autoroute.models import AutoroutingModel


class SlugIncludedModel(AutoroutingModel):
    slug = models.SlugField(max_length=255, unique=True)
    slug_attribute = 'name'

    def save(self, *args, **kwargs):
        self.slug = slugify(getattr(self, self.slug_attribute))
        super().save(*args, **kwargs)

    class Meta:
        abstract = True


class Tag(SlugIncludedModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Category(SlugIncludedModel):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Genre(SlugIncludedModel):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Author(SlugIncludedModel):
    name = models.CharField(max_length=255)
    birthdate = models.DateField(auto_now=False)
    bio = models.TextField()
    tags = models.ManyToManyField('Tag', related_name='authors')
    # books = models.ManyToManyField('Book')

    def __str__(self):
        return self.name


class Publisher(SlugIncludedModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Book(SlugIncludedModel):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255, blank=True)
    summary = models.TextField(blank=True)
    # review = models.TextField(blank=True)
    date_published = models.DateField(auto_now=False)
    date_added = models.DateTimeField(auto_now_add=True)
    # url = models.URLField(max_length=512, blank=True)
    rating = models.IntegerField()
    cover_art = models.URLField(max_length=512, blank=True)
    author = models.ManyToManyField(Author, related_name='books')
    tags = models.ManyToManyField(Tag, related_name='books')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='books')
    genres = models.ManyToManyField(Genre, related_name='books')
    publisher = models.ForeignKey(Publisher, related_name='books', on_delete=models.CASCADE)

    slug_attribute = 'title'

    def __str__(self):
        return self.title


class Visibility(models.Model):
    type = models.CharField(max_length=100)

    class Meta:
        abstract = True

    def __str__(self):
        return self.type


class BookVisibility(Visibility):
    pass


class BookUrl(models.Model):
    url = models.URLField(max_length=255)
    book = models.ForeignKey('Book', related_name='urls', on_delete=models.CASCADE)

    def __str__(self):
        return self.url


class Review(models.Model):
    author = models.OneToOneField('Author', on_delete=models.CASCADE, related_name='reviews')
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    published = models.BooleanField()
    contents = models.TextField()
    book = models.ForeignKey('Book', on_delete=models.CASCADE, related_name="reviews")


