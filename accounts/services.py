from django.db import IntegrityError
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate


def create_context_sign_up_user(request):
    '''Возвращает контекст для регистрации пользователя'''
    form = UserCreationForm()
    if request.method == 'GET':
        return {'form': form}
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
            except IntegrityError:
                return {'form': form, 'error': f'That username has already been taken.\n'
                                               f'Please choose a new username.'}
        else:
            return {'form': form, 'error': 'Passwords did not match'}


def create_context_sign_in_user(request):
    '''Возвращает контекст для входа пользователя'''
    form = AuthenticationForm()
    if request.method == 'GET':
        return {'form': form}
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return {'form': form, 'error': 'Username and password did not match'}
        else:
            login(request, user)
            return redirect('home')
