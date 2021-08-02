from django.urls import path
from .views import UploadFileView, NewUploadFileView, MultipleUploadFileView
urlpatterns = [
    path('uploadfile', UploadFileView.as_view()),
    path('newuploadfile', NewUploadFileView.as_view()),
    path('multifile', MultipleUploadFileView.as_view()),
]