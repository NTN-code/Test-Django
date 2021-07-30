from django.urls import path
from client.views import AuthClientView, AuthClientLoginView, MainPageView, LogOut1ClientView, LogOut2ClientView

urlpatterns = [
    path('client/', AuthClientView.as_view(), name='login'),
    path('another_client/', AuthClientLoginView.as_view(), name='another_login'),
    path('main/', MainPageView.as_view(), name='main'),
    path('logout1/', LogOut1ClientView.as_view(), name='logout1'),
    path('logout2/', LogOut2ClientView.as_view(), name='logout2'),
]
