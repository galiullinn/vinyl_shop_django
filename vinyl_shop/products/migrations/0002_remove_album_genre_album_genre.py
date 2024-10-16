# Generated by Django 4.2 on 2024-10-16 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='genre',
        ),
        migrations.AddField(
            model_name='album',
            name='genre',
            field=models.ManyToManyField(to='products.genre'),
        ),
    ]
