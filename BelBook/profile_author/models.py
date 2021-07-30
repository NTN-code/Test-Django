from django.db import models


# Create your models here.


class Authors(models.Model):
    STYLE_TYPE = [
        ('anc Greek', 'Ancient Greek Literatura'),
        ('anc Roma', 'Ancient Roma Literatura'),
        ('anc Belarus', 'Ancient Belarus Literatura'),
    ]

    name = models.CharField(max_length=30, verbose_name='Имя', null=False, blank=False)
    surname = models.CharField(max_length=30, verbose_name='Фамилия', null=False, blank=False)
    genre = models.TextField(verbose_name='Жанр', null=True, blank=True)
    language = models.TextField(verbose_name='Язык', null=False, blank=False)
    description = models.TextField(verbose_name='Описание', null=True, blank=True)
    email = models.EmailField(verbose_name='Email')
    birthday = models.DateTimeField(db_index=True, verbose_name='Дата рождения')
    style = models.CharField(max_length=20, choices=STYLE_TYPE, default='anc Belarus', null=False, blank=False,
                             verbose_name='Стиль литературы')


    class Meta:
        db_table = 'Authors'
        verbose_name_plural = "Авторы"
        verbose_name = "Автор"
        ordering = ['surname']

    def __str__(self):
        return f'{self.name} {self.surname}'


class AuthorsStatus(models.Model):
    name = models.CharField(max_length=100, verbose_name='Статус')

    class Meta:
        db_table = 'AuthorsStatus'
        verbose_name_plural = "Статусы"
        verbose_name = 'Статус'
        ordering = ['name']
