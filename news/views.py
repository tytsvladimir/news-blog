from django.shortcuts import render, get_object_or_404
from .models import Category, News


def home(request, pk=0):
    categories = Category.objects.all()

    def show_news(news):
        # Если есть новости, показываем, если нет, выводим сообщение
        if news:
            return render(request, 'home.html', {'page_name': categories[pk - 1].name if pk else 'News',
                                                 'news': news,
                                                 'categories': categories})
        else:
            return render(request, 'home.html', {'page_name': categories[pk - 1].name if pk else 'News',
                                                 'news': news,
                                                 'categories': categories,
                                                 'error': 'There is no news on this topic.'})

    # Если есть id категории в аргументе, то показываем новости по этой категории
    if pk:
        news = News.objects.filter(category_id=pk)
        return show_news(news)
    else:
        news = News.objects.all()
        return show_news(news)


def article(request, news_pk):
    categories = Category.objects.all()
    news = get_object_or_404(News, pk=news_pk)
    return render(request, 'article.html', {'page_name': news.title, 'news': news, 'categories': categories})
