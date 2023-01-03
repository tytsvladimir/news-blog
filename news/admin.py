from django.contrib import admin
from .models import Category, Article


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'title', 'date_of_create', 'date_of_update', 'is_published')
    list_display_links = ('id', 'category', 'title', 'date_of_create', 'date_of_update')
    search_fields = ('title', 'description', 'article')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'date_of_create', 'date_of_update')
    list_per_page = 10


admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)
