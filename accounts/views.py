from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.shortcuts import render, redirect
from django.contrib.auth import logout, login
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .utils import *
from .forms import *


class SignUpView(DataMixin, CreateView):
    form_class = SignUpViewForm
    template_name = 'accounts/sign_up_user.html'
    success_url = reverse_lazy('signin')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        c_def['page_name'] = 'Sign Up'
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class SignInView(DataMixin, LoginView):
    form_class = SignInViewForm
    template_name = 'accounts/sign_in_user.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        c_def['page_name'] = 'Sign In'
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')


def log_out_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')


def profile_view(request):
    context = {'page_name': 'Profile'}
    return render(request, 'accounts/profile.html', context=context)


def settings_view(request):
    context = {'page_name': 'Settings'}
    return render(request, 'accounts/settings.html', context=context)


class ChangeUserPasswordView(PasswordChangeView):
    '''Отображает форму для изменения пароля пользователя'''
    form_class = PasswordChangeForm
    model = User
    template_name = 'accounts/edit_password_user.html'
    extra_context = {'page_name': 'Edit password'}
    success_url = reverse_lazy('profile')
