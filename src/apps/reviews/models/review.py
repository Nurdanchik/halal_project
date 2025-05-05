from django.db import models
from common.models.base import BaseModel
from django.conf import settings

class Review(BaseModel):
    """
    Модель Отзыва.

    Аттрибуты:
    - author: пользователь, оставивший отзыв
    - stars: оценка
    - review: текст отзыва
    """

    card = models.ForeignKey("cards.Card", on_delete=models.CASCADE)

    author = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Автор отзыва'
    )

    STARS_CHOICES = [(i, str(i)) for i in range(1, 6)] 

    stars = models.PositiveSmallIntegerField(
        choices=STARS_CHOICES,
        verbose_name='Оценка (звезды)'
    )

    review = models.TextField(verbose_name='Текст отзыва')


    def __str__(self):
        return f'{self.author} - {self.stars}⭐'

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'