from django.db import models

# Create your models here.
class Movies(models.Model):
    movie_name = models.CharField(max_length=50)
    movie_desc = models.TextField()
    movie_year = models.IntegerField()
    movie_img = models.ImageField(upload_to='gallery')

    def  __str__(self):
        return self.movie_name
