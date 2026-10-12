from django.urls import path
from .views import home_view, article_detail_view, robots_txt

urlpatterns = [
    path('', home_view, name='home'),
    path('article/<slug:slug>/', article_detail_view, name='article_detail'),
    path('robots.txt', robots_txt, name='robots_txt'),
]