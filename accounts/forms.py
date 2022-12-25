from django.forms import ModelForm
from news.models import News


class NewArticleForm(ModelForm):
    class Meta:
        model = News
        fields = ['author', 'category', 'title', 'image', 'description', 'article']