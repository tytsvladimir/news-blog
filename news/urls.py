from django.urls import path
from .views import *


urlpatterns = [
    # Manage articles
    path('articles/', MyArticlesView.as_view(), name='manage_articles'),
    path('categories/', ManageCategoriesView.as_view(), name='manage_categories'),
    path('new_article/', ArticleCreateView.as_view(), name='new_article'),
    path('edit_article/<int:pk>', ArticleUpdateView.as_view(), name='edit_article'),
    path('delete_article/<int:pk>', delete_article, name='delete_article'),
    path('new_category/', CategoryCreateView.as_view(), name='new_category'),
    path('edit_category/<int:pk>', CategoryEditView.as_view(), name='edit_category'),
    path('delete_category/<int:pk>', delete_category, name='delete_category'),
]