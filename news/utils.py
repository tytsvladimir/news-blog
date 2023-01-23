from .models import Article, Category


class DataMixin:
    model = Article
    context_object_name = 'news'
    # allow_empty = False
    paginate_by = 6

    def get_user_context(self, **kwargs):
        context = kwargs
        categories = Category.objects.all()
        context['categories'] = categories
        return context
