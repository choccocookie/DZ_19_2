from django.db import models


class Category(models.Model):
    category_name = models.CharField(
        max_length=50,
        verbose_name="Название категории",
        help_text="Введите название категории",
    )
    category_description = models.TextField(
        verbose_name="Описание категории",
        help_text="Опишите категорию",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Категория продуктов"
        verbose_name_plural = "Категории продуктов"
        ordering = ["category_name"]

    def __str__(self):
        return self.category_name


class Product(models.Model):
    product_name = models.CharField(
        max_length=50,
        verbose_name="Название продукта",
        help_text="Введите название продукта",
    )
    product_description = models.TextField(
        verbose_name="Описание продукта",
        help_text="Опишите продукт",
        blank=True,
        null=True,
    )
    image = models.ImageField(
        upload_to="catalog/photo",
        blank=True,
        null=True,
        help_text="Загрузите фото продукта",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name="Категория продукта",
        help_text="Введите категорию продукта",
        blank=True,
        null=True,
        related_name="categories",
    )
    purchase_price = models.CharField(
        max_length=30, verbose_name="Цена продукта", help_text="Введите цену продукта"
    )
    created_at = models.DateField(
        verbose_name="Дата создания продукта",
        help_text="Введите дату создания продукта",
        blank=True,
        null=True,
    )
    updated_at = models.DateField(
        verbose_name="Дата изменения продукта",
        help_text="Введите дату изменения продукта",
        blank=True,
        null=True,
    )


    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["product_name", "category", "purchase_price"]

    def __str__(self):
        return self.product_name
