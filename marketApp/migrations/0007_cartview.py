# Generated by Django 5.1.1 on 2024-09-16 05:15

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketApp', '0006_alter_category_photo_alter_category_slug_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CartView',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1, verbose_name='Количество')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_owner', to=settings.AUTH_USER_MODEL, verbose_name='Владелец')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_product', to='marketApp.product', verbose_name='Продукт')),
            ],
            options={
                'verbose_name': 'Корзина',
                'verbose_name_plural': 'Корзины',
                'ordering': ['product'],
            },
        ),
    ]