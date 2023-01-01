from django.urls import path
from .views import *


urlpatterns = [
    # Manage articles
    path('', manage, name='manage'),
    path('new_article/', create_new_article, name='newarticle'),
    path('edit_article/<int:pk>', edit_article, name='editarticle'),
    path('delete_article/<int:pk>', delete_article, name='deletearticle'),
]