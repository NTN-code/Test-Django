from django import forms


class AuthClientForm(forms.Form):
    username = forms.CharField(max_length=18)
    password = forms.CharField(widget=forms.PasswordInput)
