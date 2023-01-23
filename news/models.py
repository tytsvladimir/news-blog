from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.urls import reverse


class Category(models.Model):
    objects = None
    name = models.CharField(max_length=32, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['-id']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home', kwargs={'cat_slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


def user_directory_path(instance, filename):
    return f'news/images/user_{instance.author.id}/' \
           f'{instance.date_of_create.year}/' \
           f'{instance.date_of_create.month}/' \
           f'{instance.date_of_create.day}/{filename}'


class Article(models.Model):
    objects = None
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    description = models.CharField(max_length=150)
    date_of_create = models.DateTimeField(auto_now_add=True)
    date_of_update = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to=user_directory_path)
    article = models.TextField()
    is_published = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'
        ordering = ['-date_of_create']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article', kwargs={'article_slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(str(self.title) + '-' + str(self.author))
        return super().save(*args, **kwargs)


class Comment(models.Model):
    article_id = models.IntegerField(verbose_name="Article's ID")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text_of_comment = models.TextField(max_length=300)
    date_of_create = models.DateTimeField(auto_now_add=True)
    date_of_update = models.DateTimeField(auto_now=True)
