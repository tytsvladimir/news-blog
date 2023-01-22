from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseNotFound, HttpResponse
from django.urls import reverse_lazy

from .forms import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import *


class ArticlesView(ListView):
    '''Отображает список всех публикаций'''
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
    '''Отображает список всех публикаций по выбранной категории'''
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


class ArticleShowView(DetailView):
    '''Отображает выбранную публикацию'''
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


class ManageArticlesView(ListView):
    '''Отображает список публикаци в личном кабинете'''
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


class ArticleCreateView(CreateView):
    '''Отображает форму для добавления новой публикации'''
    form_class = ArticleForm
    template_name = 'news/new_article.html'
    success_url = reverse_lazy('manage_articles')

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.author_id = self.request.user.id
        instance.save()
        return super().form_valid(form)


class ArticleEditView(UpdateView):
    '''Отображает форму для редактирования публикации'''
    form_class = ArticleForm
    model = Article
    template_name = 'news/edit_article.html'


def delete_article(request, pk):
    '''Удаляет публикацию'''
    news = get_object_or_404(Article, pk=pk, author=request.user.id)
    news.delete()
    return redirect('manage_articles')


class ManageCategoriesView(ListView):
    '''Отображает список всех категорий в личном кабинете'''
    model = Category
    template_name = 'news/manage_categories.html'
    context_object_name = 'categories'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        page_name = 'Categories'
        context = super().get_context_data(**kwargs)
        context['page_name'] = page_name
        return context

    def get_queryset(self):
        return Category.objects.all()


class CategoryCreateView(CreateView):
    '''Отображает форму для добавления новой публикации'''
    form_class = CategoryForm
    template_name = 'news/new_category.html'
    success_url = reverse_lazy('manage_categories')


class CategoryEditView(UpdateView):
    '''Отображает форму для редактирования категории'''
    form_class = CategoryForm
    model = Category
    template_name = 'news/edit_category.html'


def delete_category(request, pk):
    '''Удаляет категорию'''
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return redirect('manage_categories')
