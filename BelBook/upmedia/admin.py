from django.contrib import admin
from .models import UploadFileModel
# Register your models here.

@admin.register(UploadFileModel)
class UploadFileAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'date_create']
