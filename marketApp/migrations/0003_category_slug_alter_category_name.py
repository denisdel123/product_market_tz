# Generated by Django 5.1.1 on 2024-09-11 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketApp', '0002_alter_category_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, max_length=30, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(help_text='Введите название категории', max_length=30, unique=True, verbose_name='Наименование'),
        ),
    ]
