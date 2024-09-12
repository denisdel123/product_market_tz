from django.db import models

from transliterate import translit, slugify

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
            transliterated_name = translit(self.name, language_code='ru', reversed=False)
            self.slug = slugify(transliterated_name)
            print(f'Saving category with slug: {self.slug}')
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']


class Subcategory(models.Model):
    photo = models.ImageField(
        upload_to='subcategory/',
        **NULLABLE, verbose_name='Картинка',
        help_text='Загрузите картинку',
    )

    name = models.CharField(
        max_length=30,
        verbose_name='Наименование',
        help_text='Введите наименование',
        unique=True
    )
    slug = models.SlugField(
        max_length=30,
        unique=True,
        **NULLABLE
    )
    associated_category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name='Категории',
        related_name='related_category',
        help_text='Выберете категорию'
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            transliterated_name = translit(self.name, language_code='ru', reversed=False)
            self.slug = transliterated_name
        return super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'
        ordering = ['name']
