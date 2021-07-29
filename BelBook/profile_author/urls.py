from django.urls import path
from .views import AuthorFromView, AuthorEditFromView


urlpatterns = [
    path('register/author', AuthorFromView.as_view(), name='register author'),
    path('author/edit/<int:author_id>', AuthorEditFromView.as_view()),
]