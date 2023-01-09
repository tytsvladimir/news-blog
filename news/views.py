from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseNotFound, HttpResponse
from .services import *


def show_article_list(request, cat_pk=0):
    '''Показывает все публикации.
    Если передан pk категории, показывает публикации по этой категории'''
    context = create_context_for_all(pk=cat_pk)
    return render(request, template_name='news/home.html', context=context)


def show_article(request, article_slug):
    '''Показывает определенную статью'''
    context = create_context_for_one(slug=article_slug)
    return render(request, template_name='news/article.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound(f'<h1>Page not found</h1>\n{exception}')


def manage_articles(request):
    articles = Article.objects.filter(author=request.user.id).order_by('-date_of_create')
    return render(request, 'news/manage_articles.html', {'articles': articles})


def create_new_article(request):
    '''Показывает форму для создания новой статьи'''
    template = 'news/new_article.html'
    context = create_context_for_new_article(request=request)
    if isinstance(context, dict):
        return render(request, template_name=template, context=context)
    else:
        return redirect('manage_articles')


def edit_article(request, pk):
    '''Показывает форму для редактирования существующей статьи'''
    template = 'news/edit_article.html'
    context = create_context_for_edit_article(request=request, pk=pk)
    if isinstance(context, dict):
        return render(request, template_name=template, context=context)
    else:
        return redirect('home')


def delete_article(request, pk):
    news = get_object_or_404(Article, pk=pk, author=request.user.id)
    news.delete()
    return redirect('manage_articles')


def manage_categories(request):
    categories = Category.objects.all()
    return render(request, 'news/manage_categories.html', {'categories': categories})


def new_category(request):
    template = 'news/new_category.html'
    context = create_context_for_new_category(request=request)
    if isinstance(context, dict):
        return render(request, template_name=template, context=context)
    else:
        return redirect('manage_categories')


def edit_category(request, pk):
    '''Показывает форму для редактирования существующей категории'''
    template = 'news/edit_category.html'
    context = create_context_for_edit_category(request=request, pk=pk)
    if isinstance(context, dict):
        return render(request, template_name=template, context=context)
    else:
        return redirect('manage_categories')


def delete_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return redirect('manage_categories')
