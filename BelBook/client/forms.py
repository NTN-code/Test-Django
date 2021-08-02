from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class AuthClientForm(forms.Form):
    username = forms.CharField(max_length=18)
    password = forms.CharField(widget=forms.PasswordInput)


class ExtendUserFormRegister(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Имя')
    last_name = forms.CharField(max_length=30, required=False, help_text='Фамилия')
    date_of_birthday = forms.DateField(required=True, help_text='Дата рождения')
    city = forms.CharField(required=True, max_length=30, help_text='Город')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2')


