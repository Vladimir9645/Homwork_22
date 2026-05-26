from django.core.management import call_command
from django.db import transaction
from catalog.models import Product

@transaction.atomic
def load_fixtures():
    # Загружаем категории (без проблем с датами)
    call_command('loaddata', 'categories.json')

    # Создаём продукты вручную с корректными датами
    products_data = [
        {
            'name': 'Смартфон',
            'description': 'Современный смартфон с камерой 48Мп',
            'price': 29999.99,
            'category_id': 1
        }
    ]

    for data in products_data:
        Product.objects.create(**data)

if __name__ == '__main__':
    load_fixtures()
