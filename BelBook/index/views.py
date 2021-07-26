from django.shortcuts import render
from .models import Book
from django.views import generic
# Create your views here.


class BookListView(generic.ListView):
    model = Book
    template_name = 'index/booklistview.html'
    context_object_name = 'books_list'
    queryset = Book.objects.all()[:6]


