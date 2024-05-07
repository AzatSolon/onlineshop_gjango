from django.db import models

NULLABLE = {"blank": True, "null": True}


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование', help_text='Название продукта')
    description = models.TextField(verbose_name="Описание", help_text="Введите описание")

    def __str__(self):
        return self.description

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
    data_last_save = models.DateField(verbose_name="дата последнего изменеия", **NULLABLE)

    def __str__(self):
        return f"{self.name}: {self.description}"

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = 'Продукты'
