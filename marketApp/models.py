from django.db import models

from transliterate import translit, slugify

from app.constants import NULLABLE
from usersApp.models import User


class Category(models.Model):
    photo = models.ImageField(
        upload_to='category/',
        help_text='Загрузите картинку',
        **NULLABLE,
        verbose_name='Картинка'
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
        **NULLABLE,
        verbose_name='slug'
    )

    def save(self, *args, **kwargs):
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
    associated_category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name='Категории',
        related_name='related_category',
        help_text='Выберете категорию'
    )
    slug = models.SlugField(
        max_length=30,
        unique=True,
        **NULLABLE,
        verbose_name='slug'
    )

    def save(self, *args, **kwargs):
        transliterated_name = translit(self.name, language_code='ru', reversed=False)
        self.slug = slugify(transliterated_name)
        print(f'Saving category with slug: {self.slug}')
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'
        ordering = ['name']


class Product(models.Model):
    image_small = models.ImageField(
        upload_to='products/small/',
        verbose_name="Изображение (маленькое)",
        help_text='Загрузите изображение',
        **NULLABLE
    )
    image_medium = models.ImageField(
        upload_to='products/medium/',
        verbose_name="Изображение (среднее)",
        help_text='Загрузите изображение',
        **NULLABLE
    )
    image_large = models.ImageField(
        upload_to='products/large/',
        verbose_name="Изображение (большое)",
        help_text='Загрузите изображение',
        **NULLABLE
    )
    name = models.CharField(
        max_length=30,
        verbose_name='Продукт',
        help_text='Введите наименование',

    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Стоимость',
        help_text='Введите стоимость'
    )
    slug = models.SlugField(
        max_length=30,
        verbose_name='slug',
        **NULLABLE
    )
    associated_subcategory = models.ForeignKey(
        Subcategory,
        on_delete=models.CASCADE,
        related_name='related_subcategory',
        verbose_name='Подкатегории',
        help_text='выберете категорию'
    )

    def save(self, *args, **kwargs):
        transliterated_name = translit(self.name, language_code='ru', reversed=False)
        self.slug = slugify(transliterated_name)
        print(f'Saving category with slug: {self.slug}')
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['name']


class CartView(models.Model):
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='related_owner',
        verbose_name='Владелец'
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='related_product',
        verbose_name='Продукт'
    )
    quantity = models.PositiveIntegerField(
        default=1,
        verbose_name='Количество'
    )

    def __str__(self):
        return f'{self.product.name} (x{self.quantity})'

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'
        ordering = ['product']
