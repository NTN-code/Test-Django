from django import forms
from .models import UploadFileModel

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=30, help_text='название')
    description = forms.CharField(max_length=100)
    file = forms.FileField()

class DocumentsSaverForm(forms.ModelForm):
    class Meta:
        model = UploadFileModel
        fields = ('title', 'description', 'file')


class MultiFileForm(forms.Form):
    file = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
