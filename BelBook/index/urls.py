from django.urls import path
from index.views import BookListView


urlpatterns = [
    path('books', BookListView.as_view(), name='booklistview')
]