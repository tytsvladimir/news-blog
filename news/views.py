from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseNotFound
from .models import Category, Article


def home(request, pk=0):
    # Если есть id категории в аргументе, то показываем новости по этой категории
    categories = Category.objects.all()
    news = Article.objects.filter(category_id=pk).order_by('-date_of_create') if pk else Article.objects.all().order_by('-date_of_create')
    context = {'page_name': categories[pk - 1].name if pk else 'News', 'news': news,
               'categories': categories, 'error': 'There is no news on this topic.'}
    return render(request, template_name='home.html', context=context)


def article(request, news_pk):
    categories = Category.objects.all()
    try:
        news = Article.objects.get(pk=news_pk)
        context = {'page_name': news.title, 'news': news, 'categories': categories}
        return render(request, template_name='article.html', context=context)
    except Article.DoesNotExist:
        context = {'page_name': 'Does Not Exist', 'categories': categories, 'error': 'This article does not exist'}
        return render(request, template_name='article.html', context=context)

def pageNotFound(request, exception):
    return HttpResponseNotFound(f'<h1>Page not found</h1>\n{exception}')