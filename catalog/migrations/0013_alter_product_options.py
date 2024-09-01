# Generated by Django 5.0.7 on 2024-09-01 12:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0012_alter_version_version_number"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="product",
            options={
                "ordering": ["name", "category", "purchase_price"],
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
