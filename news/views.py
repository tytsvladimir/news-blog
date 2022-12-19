from django.shortcuts import render, get_object_or_404
from .models import News


def home(request):
    news = News.objects.all()
    return render(request, 'home.html', {'page_name': 'News', 'news': news})


def tech_science(request):
    news = News.objects.filter(category='Science and Technology')
    if news:
        return render(request, 'home.html', {'page_name': 'Science and Technology', 'news': news})
    else:
        return render(request, 'home.html',
                      {'page_name': 'Science and Technology', 'error': 'There is no news on this topic.'})


def economy(request):
    news = News.objects.filter(category='Economy')
    if news:
        return render(request, 'home.html', {'page_name': 'Economy', 'news': news})
    else:
        return render(request, 'home.html', {'page_name': 'Economy', 'error': 'There is no news on this topic.'})


def business(request):
    news = News.objects.filter(category='Business')
    if news:
        return render(request, 'home.html', {'page_name': 'Business', 'news': news})
    else:
        return render(request, 'home.html', {'page_name': 'Business', 'error': 'There is no news on this topic.'})


def culture(request):
    news = News.objects.filter(category='Culture')
    if news:
        return render(request, 'home.html', {'page_name': 'Culture', 'news': news})
    else:
        return render(request, 'home.html', {'page_name': 'Culture', 'error': 'There is no news on this topic.'})


def ideas(request):
    news = News.objects.filter(category='Ideas')
    if news:
        return render(request, 'home.html', {'page_name': 'Ideas', 'news': news})
    else:
        return render(request, 'home.html', {'page_name': 'Ideas', 'error': 'There is no news on this topic.'})


def article(request, news_pk):
    news = get_object_or_404(News, pk=news_pk)
    return render(request, 'article.html', {'page_name': news.title, 'news': news})