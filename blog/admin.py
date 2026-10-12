from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Category, Article, ProductAffiliate

class ProductInline(admin.TabularInline):
    model = ProductAffiliate
    extra = 1

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ProductInline]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
