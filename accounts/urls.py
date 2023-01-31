from django.urls import path, include
from .views import *

urlpatterns = [
    # Auth
    path('signup/', SignUpView.as_view(), name='signup'),
    path('logout/', log_out_view, name='logout'),
    path('signin/', SignInView.as_view(), name='signin'),

    # Profile
    path('profile/', profile_view, name='profile'),
    path('profile/settings/', settings_view, name='settings'),
    path('profile/edit_password_user/', ChangeUserPasswordView.as_view(), name='edit_password_user'),
    path('profile/manage/', include('news.urls')),
]
