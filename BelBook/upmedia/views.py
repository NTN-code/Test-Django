from django.shortcuts import render, redirect
from django.views import View
from .forms import UploadFileForm, DocumentsSaverForm, MultiFileForm
from django.http import HttpResponse
from .models import UploadFileModel

# Create your views here.


class UploadFileView(View):
    def get(self, request):
        form = UploadFileForm()
        return render(request, 'UploadFile.html', context={'form': form})

    def post(self, request):
        data = UploadFileForm(request.POST, request.FILES)
        if data.is_valid():
            file = request.FILES['file']
            return HttpResponse(content=file.name, status=200)


class NewUploadFileView(View):
    def get(self, request):
        form = DocumentsSaverForm()
        return render(request, 'newUploadFile.html', context={'form': form})

    def post(self, request):
        form = DocumentsSaverForm(request.POST, request.FILES)
        if form.is_valid():
            # file = request.FILES['file']
            form.save()
            return redirect('/')

class MultipleUploadFileView(View):
    def get(self, request):
        form = MultiFileForm()
        return render(request, 'newUploadFile.html', context={'form': form})

    def post(self, request):
        form = MultiFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES.getlist('file_field')
            for f in file:
                instant = UploadFileModel(file=f)
                instant.save()
            return redirect('/')