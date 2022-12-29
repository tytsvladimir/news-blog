from django.forms import ModelForm
from news.models import Article


class NewArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['category', 'title', 'image', 'description', 'article']