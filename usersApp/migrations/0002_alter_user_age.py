# Generated by Django 5.1.1 on 2024-09-16 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usersApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Age'),
        ),
    ]