from django.shortcuts import render
from .models import News

# Create your views here.
def home(request):
    news = News.objects.all()
    return render(request, 'home.html', {'page_name':'Home page', 'news': news})