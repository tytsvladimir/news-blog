from django.shortcuts import get_object_or_404
from .models import Category, Article
from news.forms import NewArticleForm


def create_context_for_all(pk: int) -> dict:
    '''Возвращает контекст для просмотра списка статей'''
    categories = Category.objects.all()
    if not pk:
        page_name = 'News'
        news = Article.objects.all().order_by('-date_of_create')
        error = 'There is no news.'
    else:
        page_name = categories[pk - 1].name
        news = Article.objects.filter(category_id=pk).order_by('-date_of_create')
        error = 'There is no news on this topic.'

    return {'page_name': page_name, 'news': news, 'categories': categories, 'error': error}


def create_context_for_one(pk: int) -> dict:
    '''Возвращает контекст для просмотра определенной статьи'''
    categories = Category.objects.all()
    error = 'This article does not exist'
    try:
        news = Article.objects.get(pk=pk)
        page_name = news.title
    except Article.DoesNotExist:
        news = None
        page_name = 'News'

    return {'page_name': page_name, 'news': news, 'categories': categories, 'error': error}


def create_context_for_new_article(request):
    '''Возвращает контекст для отображения формы создания новой статьи'''
    if request.method == 'GET':
        form = NewArticleForm()
        return {'form': form}
    else:
        form = NewArticleForm(request.POST, request.FILES)
        error = form.errors
        if form.is_valid():
            article = form.save(commit=False)
            article.author_id = request.user.id
            article.save()
        else:
            return {'form': form, 'error': error}


def create_context_for_edit_article(request, pk):
    '''Возвращает контекст для отображения формы редактирования статьи'''
    article = get_object_or_404(Article, pk=pk, author=request.user.id)
    if request.method == 'GET':
        form = NewArticleForm(instance=article)
        return {'form': form, 'pk': pk}
    else:
        form = NewArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
        else:
            return {'form': form, 'pk': pk, 'error': form.errors}
