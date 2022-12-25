from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=32)

    class Meta:
        verbose_name_plural = 'Category'

    def __str__(self):
        return self.name


class News(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE, auto_created=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=150)
    image = models.ImageField(upload_to='news/images/')
    article = models.TextField()
    date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'News'

    def __str__(self):
        return self.title
