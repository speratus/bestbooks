from django.db import models

from django.template.defaultfilters import slugify


class SlugIncludedModel(models.Model):
    slug = models.SlugField(max_length=255)
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


class Book(SlugIncludedModel):
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

    slug_attribute = 'title'

    def __str__(self):
        return self.title

