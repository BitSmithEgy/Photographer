# models.py
from django.db import models

class Package(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='packages/', blank=True)
    VIDEOPGRAPHY = 'videography'
    CINEMA = 'cinema'

    FIELD_CHOICES = [
        (VIDEOPGRAPHY, 'Videography'),
        (CINEMA, 'Cinema'),
    ]

    field = models.CharField(
        max_length=20,
        choices=FIELD_CHOICES,
        default=VIDEOPGRAPHY,
    )

    def __str__(self):
        return self.title

class Video(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    video_file = models.FileField(upload_to='videos/')
    upload_date = models.DateTimeField(auto_now_add=True)
    poster = models.ImageField(upload_to='posters/', blank=True, default='media/Screen Shot 2024-01-15 at 05.01.44.png')
    drive_link = models.TextField(blank=True)
    def __str__(self):
        return self.title
    

class HomeVideo(models.Model):
    video = models.FileField(upload_to='videos/')

class Videographer(models.Model):
    name = models.CharField(max_length = 100, blank=True)
    projects = models.PositiveSmallIntegerField(blank=True)
    image = models.ImageField(upload_to='videographers/')
    slogen = models.TextField(blank=True)

    def __str__(self):
        return self.name