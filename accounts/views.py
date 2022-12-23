from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

def sign_up_user(request):
    if request.method == 'GET':
        return render(request, 'accounts/sign_up_user.html', {'form': UserCreationForm()})
