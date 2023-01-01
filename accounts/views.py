from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .services import create_context_sign_up_user, create_context_sign_in_user


def sign_up_view(request):
    '''Показывает форму регистрации'''
    template = 'accounts/sign_up_user.html'
    context = create_context_sign_up_user(request=request)
    if isinstance(context, dict):
        return render(request, template_name=template, context=context)
    else:
        return redirect('profile')


def sign_in_view(request):
    '''Показывает форму входа в личный кабинет'''
    template = 'accounts/sign_in_user.html'
    context = create_context_sign_in_user(request=request)
    if isinstance(context, dict):
        return render(request, template_name=template, context=context)
    else:
        return redirect('profile')


def log_out_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')


def profile_view(request):
    return render(request, 'accounts/profile.html')
