from django.db import models
from common.models.base import BaseModel


class Category(BaseModel):
    """
    Модель категорий заведений (кафе, ресторан, магазин...).
    """
    name = models.CharField(max_length=100, unique=True, verbose_name='Название категории')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'