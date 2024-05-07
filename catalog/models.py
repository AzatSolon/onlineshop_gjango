from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование', help_text='Название продукта')
    description = models.CharField(max_length=150, verbose_name='Описание', help_text='Информация о продукте')
    image = models.ImageField(upload_to='catalog/photo', blank=True, null=True, verbose_name='Фото',
                              help_text='Загрузите фото')
    price = models.IntegerField(verbose_name='Цена', help_text='Цена за покупку')
    data_make = models.DateField(blank=True, null=True, verbose_name='Дата создания', help_text='Дата записи в БД')
    data_last_save = models.DateField(auto_now_add=True, auto_created=True, blank=True, null=True,
                                      verbose_name='Дата посленего изменения',
                                      help_text='Дата последнего изменения в БД')
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, verbose_name='Категория',
                                 help_text='Выберите категорию',
                                 null=True, blank=True, related_name='products', )

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['name', 'category']

    def __str__(self):
        return f"{self.name} {self.description} {self.price}"


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование', help_text='Название продукта')
    description = models.CharField(max_length=150, verbose_name='Описание', help_text='Информация о продукте')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']

    def __str__(self):
        return f"{self.name} {self.description}"
