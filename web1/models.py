from django.db import models

# Create your models here.

class Team(models.Model):
    id: int
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='static/img')
    designation = models.TextField()
    description = models.TextField()