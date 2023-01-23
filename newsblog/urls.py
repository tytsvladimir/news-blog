from django.contrib import admin
from django.urls import path, include
from news import views as news_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', news_views.ArticlesView.as_view(), name='home'),
    path('category/<slug:cat_slug>/', news_views.ArticlesCategoryView.as_view(), name='home'),
    path('article/<slug:article_slug>/', news_views.ArticleShowView.as_view(), name='article'),

    # Auth
    path('accounts/', include('accounts.urls')),
]

# if settings.DEBUG:
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# 404
handler404 = news_views.pageNotFound
