from django.urls import path
from index.views import BookListView, BookDetailListView


urlpatterns = [
    path('books', BookListView.as_view(), name='booklistview'),
    path('books/<int:pk>', BookDetailListView.as_view(), name='bookdetaillistview'),
]