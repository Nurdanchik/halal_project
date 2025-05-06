from django.db import models
from common.models.base import BaseModel


class Card(BaseModel):
    """
    Модель Карточки заведения.

    Аттрибуты:
    - face_img: главное фото
    - whatsapp: ссылка на WhatsApp
    - telegram: ссылка на Telegram
    - site: ссылка на сайт
    - description: описание
    - start_work: время начала работы
    - stops_work: время окончания работы
    - work_days: дни работы
    - location: ссылка на локацию
    - category: категория
    - title: название заведения
    - address: полный адрес
    - type: тип заведения
    - video: видео
    """

    TYPE_CHOICES = [
        ('food', 'Еда'),
        ('religion', 'Религия'),
        ('services', 'Услуги'),
        ('business', 'Работа и бизнес'),
        ('family', 'Семья и дети'),
    ]

    face_img = models.ImageField(
        upload_to='cards/faces/',
        verbose_name='Главное фото'
    )

    type = models.CharField(
        max_length=20,
        choices=TYPE_CHOICES,
        verbose_name='Тип заведения'
    )   
     
    address = models.CharField(
        max_length=255,
        verbose_name='Полный адрес',
        help_text='Например: г. Бишкек, ул. Ленина, 25'
    ) 

    title = models.CharField(
        max_length=100,
        verbose_name='Название заведения'
    )

    category = models.ForeignKey(
    to='categories.Category',
    on_delete=models.SET_NULL,
    null=True,
    blank=True,
    related_name='cards',
    verbose_name='Категория',
    )   

    phone_number = models.CharField(
    max_length=20,
    verbose_name='Номер телефона',
    help_text='Например: +996707123456',
    blank=True,
    null=True
    )

    whatsapp = models.URLField(
        blank=True,
        null=True,
        verbose_name='Ссылка на WhatsApp'
    )

    telegram = models.URLField(
        blank=True,
        null=True,
        verbose_name='Ссылка на Telegram'
    )

    site = models.URLField(
        blank=True,
        null=True,
        verbose_name='Сайт'
    )

    description = models.TextField(
        verbose_name='Описание'
    )

    start_work = models.TimeField(
        verbose_name='Время открытия'
    )

    stops_work = models.TimeField(
        verbose_name='Время закрытия'
    )

    work_days = models.CharField(
        max_length=50,
        verbose_name='Дни работы',
        help_text='например: Пн-Вс или Пн-Пт'
    )

    video = models.FileField(
        upload_to='cards/videos/',
        blank=True,
        null=True,
        verbose_name='Видео заведения'
    )

    location = models.ForeignKey(
        'cards.Place',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='cards',
        verbose_name='Локация'
    )

    def __str__(self):
        return f'{self.description[:30]}...'

    class Meta:
        verbose_name = 'Карточка'
        verbose_name_plural = 'Карточки'


class CardPhoto(BaseModel):
    """
    Модель дополнительных фотографий заведения
    """
    card = models.ForeignKey(Card, on_delete=models.CASCADE, related_name='photos', verbose_name='Карточка')
    image = models.ImageField(upload_to='cards/photos/', verbose_name='Фото')

    def __str__(self):
        return f'Фото для {self.card}'
    
    class Meta:
        verbose_name = 'Фото заведения'
        verbose_name_plural = 'Фотки заведения'