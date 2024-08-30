from django.urls import path
from hexlet_django_blog.article import views
from django.shortcuts import redirect
from django.urls import reverse

urlpatterns = [
    path('', views.HomePageView.as_view(), name='index'),
    path('tags/<str:tags>/<int:article_id>/', views.ArticleIndexView.as_view(), name='article'),
]