"""newsblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from news import views as news_views
from accounts import views as accounts_views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', news_views.home, name='home'),
    path('news/<int:pk>/', news_views.home, name='news'),
    path('<int:news_pk>/', news_views.article, name='article'),

    # Auth
    path('signup/', accounts_views.sign_up_user, name='signup'),
    path('logout/', accounts_views.log_out_user, name='logout'),
    path('signin/', accounts_views.sign_in_user, name='signin'),

    # Profile
    path('profile/', include('accounts.urls')),
]

# if settings.DEBUG:
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# 404
handler404 = news_views.pageNotFound