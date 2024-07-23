from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name="Название категории",
        help_text="Введите название категории",
    )
    description = models.TextField(
        verbose_name="Описание категории",
        help_text="Опишите категорию",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Категория продуктов"
        verbose_name_plural = "Категории продуктов"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name="Название продукта",
        help_text="Введите название продукта",
    )
    description = models.TextField(
        verbose_name="Описание продукта",
        help_text="Опишите продукт",
        blank=True,
        null=True,
    )
    image = models.ImageField(
        upload_to="products/photo",
        blank=True,
        null=True,
        help_text="Загрузите фото продукта",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name="Категория продукта",
        help_text="Введите категорию продукта",
        blank=True,
        null=True,
        related_name="categories",
    )
    purchase_price = models.IntegerField(
        verbose_name="Цена продукта",
        help_text="Введите цену продукта"
    )
    created_at = models.DateTimeField(
        verbose_name="Дата создания продукта",
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        verbose_name="Дата изменения продукта",
        auto_now=True,
    )


    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name", "category", "purchase_price"]

    def __str__(self):
        return self.name

class ContactInfo(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return self.name