from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.shortcuts import redirect
from django.urls import reverse

# Create your views here.
class ArticleIndexView(View):
    def get(self, request, tags=None, article_id=None):
        if tags is not None and article_id is not None:
            context = {
                'app_name': 'Hexlet Django Blog Article',
                'message': f'Статья номер {article_id}. Тег {tags}'
            }
        else:
            context = {
                'app_name': 'Hexlet Django Blog Article',
                'message': 'Добро пожаловать в Hexlet Django Blog Article!'
            }
        return render(request, 'articles/index.html', context)


class HomePageView(View):
    def get(self, request):
        return redirect(reverse('article', args=['python', 42]))