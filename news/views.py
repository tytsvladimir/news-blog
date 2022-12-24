from django.shortcuts import render, get_object_or_404
from .models import Category, News


def home(request, pk=0):
    # Если есть id категории в аргументе, то показываем новости по этой категории
    categories = Category.objects.all()
    news = News.objects.filter(category_id=pk).order_by('-date') if pk else News.objects.all().order_by('-date')
    context = {'page_name': categories[pk - 1].name if pk else 'News', 'news': news,
               'categories': categories, 'error': 'There is no news on this topic.'}
    return render(request, template_name='home.html', context=context)


def article(request, news_pk):
    categories = Category.objects.all()
    try:
        news = News.objects.get(pk=news_pk)
        context = {'page_name': news.title, 'news': news, 'categories': categories}
        return render(request, template_name='article.html', context=context)
    except News.DoesNotExist:
        context = {'page_name': 'Does Not Exist', 'categories': categories, 'error': 'This article does not exist'}
        return render(request, template_name='article.html', context=context)
