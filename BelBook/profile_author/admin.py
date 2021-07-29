from django.contrib import admin
from profile_author.models import Authors, AuthorsStatus
# Register your models here.


@admin.register(Authors)
class AuthorsAdmin(admin.ModelAdmin):
    pass


@admin.register(AuthorsStatus)
class AuthorsStatusAdmin(admin.ModelAdmin):
    pass