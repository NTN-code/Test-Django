from django.shortcuts import render
from .forms import AuthorForm
from django.views import View
from profile_author.models import Authors
from django.http import HttpResponseRedirect
# Create your views here.

class AuthorFromView(View):
    def get(self, request):
        author_form = AuthorForm()
        return render(request, 'register_author.html', context={'author_form': author_form})

    def post(self, request):
        author_form = AuthorForm(request.POST)
        if author_form.is_valid():
            Authors.objects.create(**author_form.cleaned_data)
            return HttpResponseRedirect('/')
        return render(request, 'register_author.html', context={'author_form': author_form})

class AuthorEditFromView(View):
    def get(self, request, author_id):
        author = Authors.objects.get(id=author_id)
        author_form = AuthorForm(instance=author)
        return render(request, 'edit_author.html', context={'author_form': author_form, 'author_id': author_id})

    def post(self, request, author_id):
        author = Authors.objects.get(id=author_id)
        author_form = AuthorForm(request.POST, instance=author)
        if author_form.is_valid():
            author.save()

        return render(request, 'edit_author.html', context={'author_form': author_form, 'author_id': author_id})
