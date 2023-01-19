from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseNotFound, HttpResponse
from django.urls import reverse_lazy

from .services import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import *


#
# def show_article_list(request, cat_pk=0):
#     '''Показывает все публикации.
#     Если передан pk категории, показывает публикации по этой категории'''
#     context = create_context_for_all(pk=cat_pk)
#     return render(request, template_name='news/home.html', context=context)

class ArticlesView(ListView):
    '''Отображение списка всех публикаций'''
    model = Article
    template_name = 'news/home.html'
    context_object_name = 'news'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        categories = Category.objects.all()
        page_name = 'News'
        context = super().get_context_data(**kwargs)
        context['page_name'] = page_name
        context['categories'] = categories
        return context

    def get_queryset(self):
        return Article.objects.filter(is_published=True)


class ArticlesCategoryView(ListView):
    '''Отображение списка публикаций по выбранной категории'''
    model = Article
    template_name = 'news/home.html'
    context_object_name = 'news'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        categories = Category.objects.all()
        page_name = categories.filter(slug=self.kwargs["cat_slug"])[0].name
        context = super().get_context_data(**kwargs)
        context['page_name'] = page_name
        context['categories'] = categories
        return context

    def get_queryset(self):
        return Article.objects.filter(category__slug=self.kwargs['cat_slug'], is_published=True)


# def show_article(request, article_slug):
#     '''Показывает определенную статью'''
#     context = create_context_for_one(slug=article_slug)
#     return render(request, template_name='news/article.html', context=context)


class ArticleShowView(DetailView):
    '''Отображение выбранной публикации'''
    model = Article
    template_name = 'news/article.html'
    slug_url_kwarg = 'article_slug'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = context[self.context_object_name].title
        return context


def pageNotFound(request, exception):
    return HttpResponseNotFound(f'<h1>Page not found</h1>\n{exception}')


# def manage_articles(request):
#     articles = Article.objects.filter(author=request.user.id).order_by('-date_of_create')
#     return render(request, 'news/manage_articles.html', {'articles': articles})


class ManageArticlesView(ListView):
    '''Отображение списка всех публикаций'''
    model = Article
    template_name = 'news/manage_articles.html'
    context_object_name = 'articles'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        page_name = 'Manage'
        context = super().get_context_data(**kwargs)
        context['page_name'] = page_name
        return context

    def get_queryset(self):
        return Article.objects.filter(author_id=self.request.user.id)


# def create_new_article(request):
#     '''Показывает форму для создания новой статьи'''
#     template = 'news/new_article.html'
#     context = create_context_for_new_article(request=request)
#     if isinstance(context, dict):
#         return render(request, template_name=template, context=context)
#     else:
#         return redirect('manage_articles')


class ArticleCreateView(CreateView):
    '''Отображение формы для добавления новой публикации'''
    form_class = ArticleForm
    template_name = 'news/new_article.html'
    success_url = reverse_lazy('manage_articles')

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.author_id = self.request.user.id
        instance.save()
        return super().form_valid(form)


# def edit_article(request, pk):
#     '''Показывает форму для редактирования существующей статьи'''
#     template = 'news/edit_article.html'
#     context = create_context_for_edit_article(request=request, pk=pk)
#     if isinstance(context, dict):
#         return render(request, template_name=template, context=context)
#     else:
#         return redirect('home')


class ArticleEditView(UpdateView):
    form_class = ArticleForm
    model = Article
    template_name = 'news/edit_article.html'


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
