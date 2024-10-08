# Generated by Django 5.1.1 on 2024-09-12 08:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketApp', '0005_alter_category_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='photo',
            field=models.ImageField(blank=True, help_text='Загрузите картинку', null=True, upload_to='category/', verbose_name='Картинка'),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, max_length=30, null=True, unique=True, verbose_name='slug'),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='slug',
            field=models.SlugField(blank=True, max_length=30, null=True, unique=True, verbose_name='slug'),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(help_text='Загрузите картинку', upload_to='product/', verbose_name='Картинка')),
                ('name', models.CharField(help_text='Введите наименование', max_length=30, verbose_name='Продукт')),
                ('price', models.PositiveIntegerField(help_text='Введите стоимость', verbose_name='Стоимость')),
                ('slug', models.SlugField(blank=True, max_length=30, null=True, verbose_name='slug')),
                ('associated_subcategory', models.ForeignKey(help_text='выберете категорию', on_delete=django.db.models.deletion.CASCADE, related_name='related_subcategory', to='marketApp.subcategory', verbose_name='Подкатегории')),
            ],
            options={
                'verbose_name': 'продукт',
                'verbose_name_plural': 'Продукты',
                'ordering': ['name'],
            },
        ),
    ]
