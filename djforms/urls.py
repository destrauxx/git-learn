from django.contrib import admin
from django.urls import path

from books.views import create_book, create_book_form, detail_book, mark_sells_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('<pk>/', create_book, name='create-book'),
    path('htmx/create-book-form/', create_book_form, name='create-book-form'),
    path('htmx/book/<pk>/', detail_book, name="detail-book"),
    path('htmx/mark_sells/<name>', mark_sells_view, name='mark-sells')
ывсмыв
]