from django.db import models
from django.utils.text import slugify

from app.constants import NULLABLE


class Category(models.Model):
    photo = models.ImageField(
        upload_to='category/',
        **NULLABLE
    )
    name = models.CharField(
        max_length=30,
        unique=True,
        verbose_name='Наименование',
        help_text='Введите название категории'
    )
    slug = models.SlugField(
        max_length=30,
        unique=True,
        **NULLABLE
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
