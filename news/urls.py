from django.urls import path
from .views import *


urlpatterns = [
    # Manage articles
    path('articles/', manage_articles, name='manage_articles'),
    path('categories/', manage_categories, name='manage_categories'),
    path('new_article/', ArticleCreateView.as_view(), name='new_article'),
    path('edit_article/<int:pk>', edit_article, name='edit_article'),
    path('delete_article/<int:pk>', delete_article, name='delete_article'),
    path('new_category/', new_category, name='new_category'),
    path('edit_category/<int:pk>', edit_category, name='edit_category'),
    path('delete_category/<int:pk>', delete_category, name='delete_category'),
]