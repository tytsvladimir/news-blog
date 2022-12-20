from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class News(models.Model):
    # CATEGORY = (('Science and Technology', 'Science and Technology'),
    #             ('Economy', 'Economy'), ('Business', 'Business'),
    #             ('Culture', 'Culture'), ('Ideas', 'Ideas'))
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=150)
    image = models.ImageField(upload_to='news/images/')
    article = models.TextField()
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
