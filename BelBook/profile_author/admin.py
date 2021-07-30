from django.contrib import admin
from profile_author.models import Authors, AuthorsStatus


# Register your models here.


@admin.register(Authors)
class AuthorsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'surname', 'genre', 'language', 'email', 'birthday', 'style']
    list_filter = ['genre', 'language', 'style']
    search_fields = ['name', 'surname', 'genre', 'language', 'email', 'style']
    fieldsets = (
        ('Информация о авторе', {
            'fields': ('name', 'surname', 'birthday', 'email'),
            'description': 'фио + др + почта'
        }),
        ('Информация о литературе', {
            'fields': ('genre', 'language', 'description', 'style'),
            'description': 'жанр + язык + + описание',
        }),
    )
    actions = ['make_as_anc_belarus', 'make_as_anc_roma', 'make_as_anc_greek']

    def make_as_anc_belarus(self, request, queryset):
        queryset.update(style='anc Belarus')

    def make_as_anc_greek(self, request, queryset):
        queryset.update(style='anc Greek')

    def make_as_anc_roma(self, request, queryset):
        queryset.update(style='anc Roma')

    make_as_anc_greek.short_description = 'Перевести стиль в древнегреческий'
    make_as_anc_roma.short_description = 'Перевести стиль в древнеримский'
    make_as_anc_belarus.short_description = 'Перевести стиль в древнебеларуский'
    pass




@admin.register(AuthorsStatus)
class AuthorsStatusAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    pass
