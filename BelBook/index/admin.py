from django.contrib import admin
from .models import Book, BookStatus
# Register your models here.

class BookInline(admin.TabularInline):
    model = Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'counter_views', 'readers', 'book_status', 'is_exist']
    list_filter = ['book_status', 'is_exist']
    search_fields = ['title', 'book_status__name']
    fieldsets = (
        ('О книге', {
            'fields': ('title', 'description', 'is_exist'),
            'description': 'инфа по книге'
        }),
        ('О количестве', {
            'fields': ('counter_views', 'readers'),
            'description': 'инфа о количестве'
        })
    )
    actions = ['make_is_exist', 'make_is_not_exist']


    def make_is_exist(self, request, queryset):
        queryset.update(is_exist=True)

    def make_is_not_exist(self, request, queryset):
        queryset.update(is_exist=False)

    make_is_exist.short_description = 'Перевести книгу в наличие'
    make_is_not_exist.short_description = 'Перевести книгу в не наличии'

    pass


@admin.register(BookStatus)
class BookStatusAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    inlines = [BookInline]
    pass



