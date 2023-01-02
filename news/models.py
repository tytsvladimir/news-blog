from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=32, db_index=True)

    class Meta:
        verbose_name_plural = 'Category'

    def __str__(self):
        return self.name

    def get_absolut_url(self):
        return reverse('home', kwargs={'cat_pk': self.pk})


class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=150)
    image = models.ImageField(upload_to='news/images/%Y/%m/%d/')
    article = models.TextField()
    date_of_create = models.DateTimeField(auto_now_add=True)
    date_of_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'News'

    def __str__(self):
        return self.title

    def get_absolut_url(self):
        return reverse('article', kwargs={'article_pk': self.pk})


class Comment(models.Model):
    article_id = models.IntegerField(verbose_name="Article's ID")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text_of_comment = models.TextField(max_length=300)
    date_of_create = models.DateTimeField(auto_now_add=True)
    date_of_update = models.DateTimeField(auto_now=True)
