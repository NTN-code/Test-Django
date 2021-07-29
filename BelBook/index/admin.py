from django.contrib import admin
from .models import Book, BookStatus
# Register your models here.


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass


@admin.register(BookStatus)
class BookStatusAdmin(admin.ModelAdmin):
    pass



