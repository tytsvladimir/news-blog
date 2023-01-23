from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms import TextInput, CharField, PasswordInput


class SignUpViewForm(UserCreationForm):
    username = CharField(label='Username', widget=TextInput(attrs={'class ': 'form-control'}))
    password1 = CharField(label='Password', widget=PasswordInput(attrs={'class ': 'form-control'}))
    password2 = CharField(label='Repeat password', widget=PasswordInput(attrs={'class ': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

class SignInViewForm(AuthenticationForm):
    username = CharField(label='Username', widget=TextInput(attrs={'class ': 'form-control'}))
    password = CharField(label='Password', widget=PasswordInput(attrs={'class ': 'form-control'}))