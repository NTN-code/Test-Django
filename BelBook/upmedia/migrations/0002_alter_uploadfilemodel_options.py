# Generated by Django 3.2.5 on 2021-08-02 12:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upmedia', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='uploadfilemodel',
            options={'ordering': ['date_create'], 'verbose_name': 'Файл', 'verbose_name_plural': 'Файлы'},
        ),
    ]
