from django.db import models

# Create your models here.
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='articles')
    content = models.TextField(help_text="Maqola matni (HTML/Markdown formatida)")
    meta_description = models.CharField(max_length=160, help_text="Google SEO uchun qisqa tavsif (max 160 belgi)")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def str(self):
        return self.title

class ProductAffiliate(models.Model):
    article = models.ForeignKey(Article, related_name='products', on_delete=models.CASCADE)
    product_name = models.CharField(max_length=200)
    amazon_link = models.URLField(help_text="Sizning Amazon Affiliate havolangiz")
    price_estimate = models.CharField(max_length=50, blank=True, null=True, help_text="Masalan: $299.99")
    pros = models.TextField(help_text="Afzalliklari (Pros)")
    cons = models.TextField(help_text="Kamchiliklari (Cons)")

    def str(self):
        return self.product_name