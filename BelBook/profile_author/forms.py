from django import forms
import datetime
from django.core.exceptions import ValidationError
from .models import Authors

# class AuthorForm(forms.Form):
#     name = forms.CharField()
#     surname = forms.CharField()
#     genre = forms.CharField(widget=forms.Textarea)
#     language = forms.CharField(widget=forms.Textarea)
#     description = forms.CharField(widget=forms.Textarea)
#     email = forms.EmailField()
#     birthday = forms.DateField()
#
#     def cleaned_birthday(self):
#         data = self.cleaned_data['birthday']
#         today = datetime.date.today()
#         delta = (today - data).days / 365
#         if delta < 18:
#             raise ValidationError('Востраст должен быть старше 18 лет!')
#         return data
#
#     def clean(self):
#         cleaned_data = super(AuthorForm, self).clean()
#         first_name = cleaned_data.get('name')
#         last_name = cleaned_data.get('surname')
#         if first_name == 'Иван' and last_name == 'Иванов':
#             msg_error = 'Нельзя чтоб было имя и фамилия Иван Иванов!'
#             self.add_error('name', msg_error)
#             self.add_error('surname', msg_error)


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Authors
        fields = '__all__'




