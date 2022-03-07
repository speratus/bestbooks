from django.contrib import admin

from .models import Tag, Category, Genre, Book, Author, BookVisibility, BookUrl, Review

admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Genre)
admin.site.register(BookVisibility)
admin.site.register(BookUrl)
admin.site.register(Review)


# admin.site.register(Book)
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    filter_horizontal = ['author', 'tags', 'genres']


# admin.site.register(Author)
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    filter_horizontal = ['tags']
