from django.db import models

NULLABLE = {"blank": True, "null": True}


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(verbose_name="Описание")

    def __str__(self):
        return f"{self.name}: {self.description}"

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="имя")
    description = models.TextField(verbose_name="описание", help_text="Введите описание")
    image = models.ImageField(upload_to="images/", verbose_name="изображение", **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, verbose_name="категория",
                                 related_name="products", **NULLABLE, )
    price = models.IntegerField(verbose_name="цена покупки")
    data_make = models.DateField(verbose_name="дата создания", **NULLABLE)
    views_counter = models.PositiveIntegerField(verbose_name='Просмотры', default=0)
    data_last_save = models.DateField(verbose_name="дата последнего изменеия", **NULLABLE)
    is_published = models.BooleanField(default=False, verbose_name='публикация')

    def __str__(self):
        return f"{self.name}: {self.description}"

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = [
            "category", "name", "price",
            "data_make", "data_last_save", 'views_counter',
            'is_published',
        ]


class Version(models.Model):
    name_product = models.ForeignKey(Product, verbose_name='название продукта продукт', on_delete=models.CASCADE,
                                     related_name='versions')
    version = models.PositiveIntegerField(verbose_name='номер версии')
    version_title = models.CharField(max_length=100, verbose_name='название версии')
    version_mark = models.BooleanField(default=True, verbose_name='признак текущей версии')

    def __str__(self):
        return f'{self.name_product} - {self.version}'

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'
