# Generated by Django 4.2.6 on 2023-10-18 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieApp', '0003_remove_movies_movie_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='movie_img',
            field=models.ImageField(default='default', upload_to='gallery'),
            preserve_default=False,
        ),
    ]
