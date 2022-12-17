from django.db import models

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=150)
    article = models.TextField()
    date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
