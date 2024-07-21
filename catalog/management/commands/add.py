from django.core.management import BaseCommand, call_command
from django.utils import timezone
import json
from catalog.models import Product, Category
from pathlib import Path

class Command(BaseCommand):

    @staticmethod
    def json_read_categories():
        base_path = Path(__file__).resolve().parent.parent.parent
        file_path = base_path / 'fixtures' / 'catalog_data.json'
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data

    @staticmethod
    def json_read_products():
        base_path = Path(__file__).resolve().parent.parent.parent
        file_path = base_path / 'fixtures' / 'product_data.json'
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data

    def handle(self, *args, **options):

        # Удалите все продукты
        Product.objects.all().delete()

        # Удалите все категории
        Category.objects.all().delete()

		# Создайте списки для хранения объектов
        product_for_create = []
        category_for_create = []

		# Обходим все значения категорий из фиктсуры для получения информации об одном объекте
        for category in Command.json_read_categories():
            category_for_create.append(
                Category(id=category['pk'], name=category['fields']['name'], description=category['fields'].get('description', ''))
            )
		# Создаем объекты в базе с помощью метода bulk_create()
        Category.objects.bulk_create(category_for_create)

		# Обходим все значения продуктов из фиктсуры для получения информации об одном объекте
        for product in Command.json_read_products():
            product_for_create.append(
                Product(id=product['pk'],
                        name=product['fields']['name'],
                        description=product['fields']['description'],
                        image=product['fields']['image'],
                        category=Category.objects.get(pk=product['fields']['category']),
                        purchase_price=product['fields']['purchase_price'],
                        created_at=product['fields'].get('created_at', ''),
                        updated_at=product['fields'].get('updated_at', '')
                        )
            )


		# Создаем объекты в базе с помощью метода bulk_create()
        Product.objects.bulk_create(product_for_create)
