from django.db import models
from django.utils import timezone


# Create your models here.

class About(models.Model):
    image_upload = models.ImageField()
    bio = models.TextField(max_length=10000, default="no content yet")

    def __str__(self):
        return self.bio
