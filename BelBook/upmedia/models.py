from django.db import models

# Create your models here.


class UploadFileModel(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(blank=True)
    file = models.FileField(upload_to='files/')
    date_create = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Файлы'
        verbose_name = 'Файл'
        ordering = ['date_create']