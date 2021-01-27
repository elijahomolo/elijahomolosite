from django.db import models
from django.utils import timezone


# Create your models here.
class Category(models.Model):
    created_at = models.DateTimeField('date created')
    updated_at = models.DateTimeField('date published')
    title = models.CharField(max_length=255)
    image = models.ImageField()

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ['title']

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField(max_length=10000, default="no content yet")
    pub_date = models.DateTimeField('date published')
    updated_at = models.DateTimeField('date updated', default=timezone.now())
    is_published = models.BooleanField(default=False, verbose_name="Publish?")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default="uncategorized")
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE, default="Elijah Omolo")
    featured = models.BooleanField(default=False)

    def publish(self):
        self.is_published = True
        self.published_at = timezone.now()
        self.save()

    def __str__(self):
        return self.title
