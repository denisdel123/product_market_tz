# Generated by Django 5.1.1 on 2024-09-16 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketApp', '0007_cartview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='photo',
            field=models.ImageField(blank=True, help_text='Загрузите картинку', null=True, upload_to='product/', verbose_name='Картинка'),
        ),
    ]
