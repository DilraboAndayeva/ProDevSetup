from django.contrib.sitemaps import Sitemap
from .models import Article
from django.urls import reverse

class ArticleSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return Article.objects.all()

    def lastmod(self, obj):
        return obj.updated_at

    def location(self, obj):
        return reverse('article_detail', args=[obj.slug])  # <-- Maqola slug yoki id'sini shu yerda bog'laymiz