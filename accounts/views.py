from django.db import IntegrityError
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from news.models import News
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import NewArticleForm
from django.contrib.auth import login, logout, authenticate


def sign_up_user(request):
    template = 'accounts/sign_up_user.html'
    # определяем что юзер хочет сделать, зарегистрироваться или войти
    if request.method == 'GET':
        return render(request, template, {'form': UserCreationForm()})
    else:
        # проверяем соответствие 2-х паролей
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                # сохраняем и логинимся
                user.save()
                login(request, user)
                return redirect('home')
            # если такой юзер уже существует
            except IntegrityError:
                return render(request, template, {'form': UserCreationForm(),
                                                  'error': f'That username has already been taken.\n'
                                                           f'Please choose a new username.'})
        else:
            return render(request, template, {'form': UserCreationForm(), 'error': 'Passwords did not match'})

def sign_in_user(request):
    template = 'accounts/sign_in_user.html'
    # определяем что юзер хочет сделать, зарегистрироваться или войти
    if request.method == 'GET':
        return render(request, template, {'form': AuthenticationForm()})
    else:
        # проверяем соответствие 2-х паролей
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, template, {'form': AuthenticationForm(), 'error': 'Username and password did not match'})
        else:
            login(request, user)
            return redirect('home')

def log_out_user(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')


def profile(request):
    articles = News.objects.filter(author=request.user.id)
    return render(request, 'accounts/profile.html', {'articles': articles})



def new_article(request):
    if request.method == 'GET':
        return render(request, 'accounts/newarticle.html', {'form': NewArticleForm()})
    else:
        form = NewArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save()
            article.author_id = request.user.id
            article.save()
            return redirect('profile')
        else:
            return render(request, 'accounts/newarticle.html', {'form': NewArticleForm(),
                                                                'error': form.errors})


def edit_article(request, pk):
    article = get_object_or_404(News, pk=pk)
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
    news = get_object_or_404(News, pk=pk)
    news.delete()
    return redirect('home')