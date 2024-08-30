# Generated by Django 5.0.7 on 2024-08-27 18:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0010_product_is_published"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="product",
            options={
                "ordering": (["name", "category", "purchase_price"],),
                "permissions": [
                    ("can_unpublish_product", "Can unpublish product"),
                    ("can_edit_description", "Can edit description"),
                    ("can_change_category", "Can change product category"),
                ],
                "verbose_name": "Продукт",
                "verbose_name_plural": "Продукты",
            },
        ),
    ]
