from django.forms import TextInput, CharField, FileField, FileInput, Textarea, CheckboxInput, ModelForm
from news.models import Article, Category


class ArticleForm(ModelForm):
    attrs = {'class ': 'form-control'}
    title = CharField(label='Username', widget=TextInput(attrs=attrs))
    description = CharField(label='Description', widget=TextInput(attrs=attrs))
    image = FileField(label='Image', widget=FileInput(attrs=attrs))
    article = CharField(label='Article', widget=Textarea(attrs=attrs))
    is_published = CheckboxInput(attrs={'class': 'form-check-input'})
    class Meta:
        model = Article
        fields = ['category', 'title', 'description', 'image', 'article', 'is_published']


class CategoryForm(ModelForm):
    attrs = {'class ': 'form-control'}
    name = CharField(label='Name', widget=TextInput(attrs=attrs))
    class Meta:
        model = Category
        fields = ['name']