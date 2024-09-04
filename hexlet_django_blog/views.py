from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.urls import reverse


# class IndexView(TemplateView):
#     template_name = "index.html"
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['who'] = 'World'
#         return context
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')
