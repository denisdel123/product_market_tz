from django.db import models

from app.constants import NULLABLE


class Category(models.Model):
    photo = models.ImageField(
        upload_to='category/',
        **NULLABLE
    )
    name = models.CharField(
        max_length=30,
        verbose_name='Наименование',
        help_text='Введите название категории'
    )

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'