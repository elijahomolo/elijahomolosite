from django.db import models

# Create your models here.
class Email(models.Model):
    email = models.EmailField(max_length=300, unique=True)

    def __str__(self):
        return self.email
