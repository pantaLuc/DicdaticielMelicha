from django.db import models

# Create your models here.

class Formation(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='Images/' , default = 'thumb-1920-1073527.png')


class Game(models.Model):
    name = models.CharField(max_length=255)
    formation = models.ForeignKey(Formation, on_delete=models.CASCADE)


class Course(models.Model):
    GENRE_CHOICES = (
        ('masculin', 'Masculin'),
        ('feminin', 'Feminin'),
    )
    title = models.CharField(max_length=255)
    types = models.CharField(max_length=10,
                             choices=GENRE_CHOICES,
                             default='masculin'
    )
    formation = models.ForeignKey(Formation, on_delete=models.CASCADE)


