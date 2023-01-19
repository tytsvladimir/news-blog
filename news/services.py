from django.db import IntegrityError
from django.shortcuts import get_object_or_404
from .models import Category, Article
from news.forms import ArticleForm, CategoryForm


# def create_context_for_all(pk: int) -> dict:
#     '''Возвращает контекст для просмотра списка статей'''
#     categories = Category.objects.all()
#     print(f'CAT ******* {categories}')
#     if not pk:
#         page_name = 'News'
#         news = Article.objects.all()[:9]  # .order_by('-date_of_create')
#         error = 'There is no news.'
#     else:
#         page_name = Category.objects.get(pk=pk).name
#         news = Article.objects.filter(category_id=pk).order_by('-date_of_create')
#         error = 'There is no news on this topic.'
#
#     return {'page_name': page_name, 'news': news, 'categories': categories, 'error': error}


def create_context_for_one(slug: str) -> dict:
    '''Возвращает контекст для просмотра определенной статьи'''
    categories = Category.objects.all()
    error = 'This article does not exist'
    try:
        # news = Article.objects.get(slug)
        news = get_object_or_404(Article, slug=slug)
        page_name = news.title
    except Article.DoesNotExist:
        news = None
        page_name = 'News'

    return {'page_name': page_name, 'news': news, 'categories': categories, 'error': error}


def create_context_for_new_article(request):
    '''Возвращает контекст для отображения формы создания новой статьи'''
    if request.method == 'GET':
        form = ArticleForm()
        return {'form': form}
    else:
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                article = form.save(commit=False)
                article.author_id = request.user.id
                article.save()
            except IntegrityError:
                return {'form': form, 'error': 'An article with this name already exists. Rename title.'}
        else:
            return {'form': form, 'error': form.errors}


def create_context_for_edit_article(request, pk):
    '''Возвращает контекст для отображения формы редактирования статьи'''
    article = get_object_or_404(Article, pk=pk, author=request.user.id)
    if request.method == 'GET':
        form = ArticleForm(instance=article)
        return {'form': form, 'pk': pk}
    else:
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
        else:
            return {'form': form, 'pk': pk, 'error': form.errors}


def create_context_for_new_category(request):
    '''Возвращает контекст для отображения формы создания новой категории'''
    if request.method == 'GET':
        form = CategoryForm()
        return {'form': form}
    else:
        form = CategoryForm(request.POST)
        if form.is_valid():
            try:
                category = form.save(commit=False)
                category.save()
            except IntegrityError:
                return {'form': form, 'error': 'A category with this name already exists. Rename title.'}
        else:
            return {'form': form, 'error': form.errors}


def create_context_for_edit_category(request, pk):
    '''Возвращает контекст для отображения формы редактирования категории'''
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'GET':
        form = CategoryForm(instance=category)
        return {'form': form, 'pk': pk}
    else:
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
        else:
            return {'form': form, 'pk': pk, 'error': form.errors}
