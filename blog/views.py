from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Article, Category

def home_view(request):
    articles = Article.objects.all().order_by('-created_at')
    categories = Category.objects.all()
    context = {
        'articles': articles,
        'categories': categories,
    }
    return render(request, 'blog/home.html', context)

def article_detail_view(request, slug):
    article = get_object_or_404(Article, slug=slug)
    context = {
        'article': article,
    }
    return render(request, 'blog/article_detail.html', context)
from django.http import HttpResponse

def robots_txt(request):
    content = """User-agent: *
Allow: /
Sitemap: http://127.0.0.1:8000/sitemap.xml
"""
    return HttpResponse(content, content_type="text/plain")