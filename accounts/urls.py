from django.urls import path, include
from . import views

urlpatterns = [
    # Auth
    path('', views.sign_up_view, name='signup'),
    path('signup/', views.sign_up_view, name='signup'),
    path('logout/', views.log_out_view, name='logout'),
    path('signin/', views.sign_in_view, name='signin'),

    # Profile
    path('profile/', views.profile_view, name='profile'),
    path('profile/manage/', include('news.urls')),
]
