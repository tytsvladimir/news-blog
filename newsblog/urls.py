from django.contrib import admin
from django.urls import path, include
from news import views as news_views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', news_views.show_article_list, name='home'),
    path('category/<int:cat_pk>/', news_views.show_article_list, name='home'),
    path('article/<slug:article_slug>/', news_views.show_article, name='article'),

    # Auth
    path('auth/', include('accounts.urls')),
]

# if settings.DEBUG:
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# 404
handler404 = news_views.pageNotFound