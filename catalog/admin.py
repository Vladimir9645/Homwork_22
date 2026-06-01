from django.contrib import admin
from .models import Product, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']  # делаем ID и название кликабельными для перехода к редактированию

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'category']
    list_filter = ['category']  # фильтрация по категории
    search_fields = ['name', 'description']  # поиск по наименованию и описанию
    list_per_page = 20  # количество элементов на странице (опционально)
