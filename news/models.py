from django.db import models

# Create your models here.
class News(models.Model):
    CATEGORY = (('Science and Technology', 'Science and Technology'),
                ('Economy', 'Economy'), ('Business', 'Business'),
                ('Culture', 'Culture'), ('Ideas', 'Ideas'))
    category = models.CharField(max_length=100, choices=CATEGORY)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=150)
    image = models.ImageField(upload_to='news/images/')
    article = models.TextField()
    date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
