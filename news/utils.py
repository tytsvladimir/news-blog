from .models import Article, Category


class DataMixin:
    model = Article
    context_object_name = 'news'
    paginate_by = 8
    # allow_empty = False

    def get_user_context(self, **kwargs):
        context = kwargs
        categories = Category.objects.all()
        context['categories'] = categories
        return context
