from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseNotFound
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .utils import *


class ArticlesView(DataMixin, ListView):
    '''Отображает список всех публикаций'''
    template_name = 'news/home.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(page_name='News', error='There is no news.')
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Article.objects.filter(is_published=True)  # select_related('category')


class ArticlesCategoryView(DataMixin, ListView):
    '''Отображает список всех публикаций по выбранной категории'''
    template_name = 'news/home.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(error='There is no news on this topic.')
        c_def['page_name'] = c_def["categories"].filter(slug=self.kwargs["cat_slug"])[0].name
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Article.objects.filter(category__slug=self.kwargs['cat_slug'], is_published=True)


class ArticleShowView(DataMixin, DetailView):
    '''Отображает выбранную публикацию'''
    template_name = 'news/article.html'
    slug_url_kwarg = 'article_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        c_def['page_name'] = context[self.context_object_name].title
        return dict(list(context.items()) + list(c_def.items()))


def pageNotFound(request, exception):
    return HttpResponseNotFound(f'<h1>Page not found</h1>\n{exception}')


class MyArticlesView(DataMixin, ListView):
    '''Отображает список публикаци в личном кабинете'''
    model = Article
    template_name = 'news/manage_articles.html'
    context_object_name = 'articles'
    paginate_by = 5
    # allow_empty = False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        c_def['page_name'] = 'My articles'
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Article.objects.filter(author_id=self.request.user.id)


class ArticleCreateView(LoginRequiredMixin, CreateView):
    '''Отображает форму для добавления новой публикации'''
    form_class = ArticleForm
    template_name = 'news/new_article.html'
    success_url = reverse_lazy('manage_articles')
    login_url = reverse_lazy('signin')
    extra_context = {'page_name': 'Create article'}

    def form_valid(self, form):
        context = form.save(commit=False)
        context.author_id = self.request.user.id
        context.save()
        return super().form_valid(form)


class ArticleUpdateView(UpdateView):
    '''Отображает форму для редактирования публикации'''
    form_class = ArticleForm
    model = Article
    template_name = 'news/edit_article.html'
    extra_context = {'page_name': 'Edit article'}


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
    extra_context = {'page_name': 'Categories'}

    def get_queryset(self):
        return Category.objects.all()


class CategoryCreateView(CreateView):
    '''Отображает форму для добавления новой публикации'''
    form_class = CategoryForm
    template_name = 'news/new_category.html'
    success_url = reverse_lazy('manage_categories')
    extra_context = {'page_name': 'Create category'}


class CategoryEditView(UpdateView):
    '''Отображает форму для редактирования категории'''
    form_class = CategoryForm
    model = Category
    template_name = 'news/edit_category.html'
    extra_context = {'page_name': 'Edit category'}


def delete_category(request, pk):
    '''Удаляет категорию'''
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return redirect('manage_categories')
