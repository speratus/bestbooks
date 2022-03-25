from django.urls import path

from . import views

urlpatterns = [
    path('book/<slug:book_slug>/', views.book_detail),
]
