# Generated by Django 4.2.6 on 2023-10-18 06:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movieApp', '0002_movies_movie_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movies',
            name='movie_img',
        ),
    ]