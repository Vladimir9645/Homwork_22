from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Название категории',
        help_text='Введите название категории'
    )

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Наименование',
        help_text='Введите наименование товара'
    )
    description = models.TextField(
        verbose_name='Описание',
        help_text='Подробное описание товара',
        blank=True,
        null=True
    )
    photo = models.ImageField(
        upload_to='products/photos/',
        blank=True,
        null=True,
        verbose_name='Изображение',
        help_text='Загрузите изображение товара'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Категория',
        help_text='Выберите категорию товара'
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Цена за покупку',
        help_text='Укажите цену товара (например, 999.99)'
    )
    created_at = models.DateTimeField(
        null=True, blank=True,
        verbose_name='Дата создания',
        help_text='Дата и время создания товара'
    )
    updated_at = models.DateTimeField(
        null=True, blank=True,
        verbose_name='Дата последнего изменения',
        help_text='Дата и время последнего обновления информации о товаре'
    )

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['-created_at']

    def __str__(self):
        return self.name
