from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context = {
        'app_name': 'Hexlet Django Blog Article',
    }
    return render(request, 'articles/index.html', context)