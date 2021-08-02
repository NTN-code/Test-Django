from django.shortcuts import render
from django.views import View
from client.forms import AuthClientForm, ExtendUserFormRegister
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
# Create your views here.
from client.models import Profile


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
        # return HttpResponse('<h1>Вы успешно вышли из учетной записи!</h1>'
        #                     '<p>TEST1</p>')
        return HttpResponseRedirect('/main/')


class LogOut2ClientView(LogoutView):
    # template_name = 'logout.html'
    next_page = '/main/'


class RegisterClientForm(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'register.html', context={'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return HttpResponseRedirect('/')

    def save(self, commit=True):
        user = super().save(commit=True)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class AnotherRegisterClientForm(View):
    def get(self, request):
        form = ExtendUserFormRegister()
        return render(request, 'register.html', context={'form': form})

    def post(self, request):
        form = ExtendUserFormRegister(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            date_of_birth = form.cleaned_data.get('date_of_birthday')
            city = form.cleaned_data.get('city')
            Profile.objects.create(
                user=user,
                city=city,
                date_of_birthday=date_of_birth,
            )
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return HttpResponseRedirect('/')

    def save(self, commit=True):
        user = super().save(commit=True)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

