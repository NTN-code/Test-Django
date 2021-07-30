from django.shortcuts import render
from django.views import View
from client.forms import AuthClientForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView, LogoutView
# Create your views here.




class AuthClientView(View):
    def get(self, request):
        client_form = AuthClientForm()
        return render(request, 'client.html', context={'form': client_form})

    def post(self, request):
        client_form = AuthClientForm(request.POST)
        if client_form.is_valid():
            username = client_form.cleaned_data['username']
            password = client_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('<h1>Вы успешно зашли</h1>')
                else:
                    client_form.add_error('__all__', 'Error user not activated!')
                    return HttpResponseRedirect('/')
            else:
                client_form.add_error('__all__', 'Error check your username and password something wrong!')
                return HttpResponseRedirect('/')


class AuthClientLoginView(LoginView):
    template_name = 'client.html'


class MainPageView(View):
    def get(self, request):
        return render(request, 'main.html')


class LogOut1ClientView(View):
    def get(self, request):
        logout(request)
        return HttpResponse('<h1>Вы успешно вышли из учетной записи!</h1>'
                            '<p>TEST1</p>')

class LogOut2ClientView(LoginView):
    template_name = 'logout.html'
