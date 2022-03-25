from django.shortcuts import render, get_object_or_404

from .models import Book


def book_detail(request, book_slug):
    book = get_object_or_404(Book, slug=book_slug)
    authors = book.author.all()
    review = book.reviews.all()

    return render(request, 'book.html', {'book': book, 'authors': authors, 'review': review})

