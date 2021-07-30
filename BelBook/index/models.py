from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False, verbose_name='Название книги')
    description = models.TextField(null=False, blank=False, verbose_name='Описание')
    url_picture = models.TextField(null=False, blank=False, verbose_name='url картинки')
    data_created = models.DateTimeField(auto_now_add=True, db_index=True, null=False, blank=False, verbose_name='Дата создания поста')
    data_update = models.DateTimeField(auto_now=True, db_index=True, null=False, blank=False, verbose_name='Дата обнавления')
    counter_views = models.IntegerField(default=0, null=False, blank=False, verbose_name='Количество просмотров')
    readers = models.IntegerField(default=0, null=False, blank=False, verbose_name='Количество читателей')
    book_status = models.ForeignKey('BookStatus', default=None, null=True, on_delete=models.CASCADE, related_name='FK_Book_book_status', verbose_name='Статус книги')
    is_exist = models.BooleanField(default=False, null=False, blank=False, verbose_name='В наличии')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'Books'
        verbose_name_plural = "Книги"
        verbose_name = 'Книга'
        ordering = ['counter_views']


class BookStatus(models.Model):
    name = models.CharField(max_length=100, verbose_name='Статус')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Статусы"
        verbose_name = 'Статус'
        ordering = ['name']