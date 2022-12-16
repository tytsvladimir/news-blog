from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html', {'page_name':'Home page'})