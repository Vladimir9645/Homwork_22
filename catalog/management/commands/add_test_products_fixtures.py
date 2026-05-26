from django.core.management.base import BaseCommand, CommandError
from django.core.management import call_command
from catalog.models import Product, Category
import os

class Command(BaseCommand):
    help = 'Удаляет данные и загружает тестовые через фикстуру (с диагностикой)'


    def handle(self, *args, **options):
        # Удаляем существующие данные
        self.stdout.write('Очистка базы данных...\n')
        Product.objects.all().delete()
        Category.objects.all().delete()

        # Загружаем фикстуры с подробной диагностикой
        self.stdout.write('Загрузка тестовых данных из фикстур...\n')

        fixtures = ['categories', 'products']

        for fixture in fixtures:
            fixture_path = f'catalog/fixtures/{fixture}.json'
            if not os.path.exists(fixture_path):
                self.stderr.write(f'✗ Файл {fixture_path} не найден!\n')
                return

            try:
                call_command('loaddata', fixture)
                self.stdout.write(
                    self.style.SUCCESS(f'✓ Фикстура {fixture} загружена успешно\n')
                )
            except CommandError as e:
                self.stderr.write(
            f'✗ Ошибка загрузки {fixture}: {e}\n'
                )
                # Дополнительная диагностика
                self._diagnose_fixture_error(fixture_path)
                return

        self.stdout.write(
            self.style.SUCCESS('✅ Все тестовые данные успешно загружены из фикстур!')
        )

    def _diagnose_fixture_error(self, filepath):
        """Дополнительная диагностика ошибок фикстуры"""
        try:
            with open(filepath, 'rb') as f:
                first_bytes = f.read(10)
                print(f"Первые байты файла: {list(first_bytes)}")
                if first_bytes[:2] == b'\xff\xfe':
                    print("⚠️  Файл в кодировке UTF-16 LE (с BOM)")
                elif first_bytes[:2] == b'\xfe\xff':
                    print("⚠️  Файл в кодировке UTF-16 BE (с BOM)")
                else:
                    print("🔎 Файл в другой кодировке")
        except Exception as e:
            print(f"Ошибка диагностики: {e}")
