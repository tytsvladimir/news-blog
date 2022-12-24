from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout


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
