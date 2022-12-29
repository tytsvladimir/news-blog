from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseNotFound

from accounts.forms import NewArticleForm
from .models import Category, Article


def home(request, pk=0):
    # Если есть id категории в аргументе, то показываем новости по этой категории
    categories = Category.objects.all()
    news = Article.objects.filter(category_id=pk).order_by('-date_of_create') if pk else Article.objects.all().order_by(
        '-date_of_create')
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


def new_article(request):
    if request.method == 'GET':
        return render(request, 'accounts/newarticle.html', {'form': NewArticleForm()})
    else:
        form = NewArticleForm(request.POST, request.FILES)
        if form.is_valid():
            print(f'******{type(form)}*******')
            article = form.save(commit=False)
            article.author_id = request.user.id
            article.save()
            return redirect('profile')
        else:
            return render(request, 'accounts/newarticle.html', {'form': NewArticleForm(),
                                                                'error': form.errors})


def edit_article(request, pk):
    article = get_object_or_404(Article, pk=pk, author=request.user.id)
    if request.method == 'GET':
        form = NewArticleForm(instance=article)
        return render(request, 'accounts/editarticle.html', {'form': form})
    else:
        form = NewArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return render(request, 'accounts/editarticle.html', {'form': form,
                                                                 'error': form.errors})


def delete_article(request, pk):
    news = get_object_or_404(Article, pk=pk, author=request.user.id)
    news.delete()
    return redirect('profile')
