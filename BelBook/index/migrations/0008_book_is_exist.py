# Generated by Django 3.2.5 on 2021-07-30 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0007_alter_book_book_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='is_exist',
            field=models.BooleanField(default=False, verbose_name='В наличии'),
        ),
    ]
