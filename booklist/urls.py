from django.urls import path

from . import views
from .models import Book, Author
from autoroute.helpers import AutoroutingModelConverter, ReadView

model_views = [
    ReadView(Book, ['slug'], ['author']),
    ReadView(Author, ['slug']),
]

urlpatterns = [
    # path('book/<slug:book_slug>/', views.book_detail),
] + AutoroutingModelConverter(model_views).gen_routes()
