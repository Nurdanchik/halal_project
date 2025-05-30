from rest_framework.generics import RetrieveAPIView
from apps.cards.models.card import Card
from apps.cards.serializers.card_full_info_serializers import CardFullInfoSerializer
from common.pagination import CustomPagination
from rest_framework.generics import ListAPIView
from apps.cards.models.card import Card
from apps.cards.models.featured_card import FeaturedCard
from apps.cards.serializers.card_serializers import CardListSerializer
from apps.cards.serializers.featured_card_serializers import FeaturedCardListSerializer
from apps.cards.serializers.type_serializers import TypeSerializer
from apps.cards.services.card_service import get_all_cards
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
from django.db.models import Q
from rest_framework import generics
from rest_framework.generics import RetrieveAPIView
from apps.cards.models.card import Card
from apps.cards.models.type import Type
from apps.cards.serializers.card_full_info_serializers import CardFullInfoSerializer
from rest_framework.exceptions import ValidationError


class CardDetailView(RetrieveAPIView):
    queryset = Card.objects.all().prefetch_related('photos', 'videos', 'reviews')
    serializer_class = CardFullInfoSerializer

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name='page',
                description='Номер страницы отзывов',
                required=False,
                type=int,
                location=OpenApiParameter.QUERY
            ),
            OpenApiParameter(
                name='page_size',
                description='Количество отзывов на странице',
                required=False,
                type=int,
                location=OpenApiParameter.QUERY
            ),
        ]
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)



class FeaturedCardListAPIView(ListAPIView):
    queryset = FeaturedCard.objects.select_related('card__category')
    serializer_class = FeaturedCardListSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['card__category']
    pagination_class = CustomPagination
    

class CardSearcherListAPIView(generics.ListAPIView):
    queryset = Card.objects.all()
    serializer_class = CardListSerializer

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name='search',
                description='Поиск по названию, типу, адресу, городу',
                required=False,
                type=str,
                location=OpenApiParameter.QUERY,
                examples=[
                    OpenApiExample(
                        "Поиск по городу Бишкек",
                        value="Бишкек",
                        summary="search=Бишкек"
                    ),
                    OpenApiExample(
                        "Поиск по адресу Navat",
                        value="Navat",
                        summary="search=Navat"
                    ),
                ],
            ),
            OpenApiParameter(
                name='city',
                description='Фильтр по городу',
                required=False,
                type=str,
                location=OpenApiParameter.QUERY,
                examples=[
                    OpenApiExample(
                        "Фильтр по городу Бишкек",
                        value="Бишкек",
                        summary="city=Бишкек"
                    )
                ],
            ),
        ],
        description=(
            "Примеры запросов:\n"
            "- /api/cards/?search=Бишкек\n"
            "- /api/cards/?search=Navat\n"
            "- /api/cards/?city=Бишкек\n"
            "- /api/cards/?city=Бишкек&search=чайхана\n"
        ),
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.query_params.get('search')
        city = self.request.query_params.get('city')

        if search:
            queryset = queryset.filter(
                Q(title__icontains=search) |
                Q(type__type__icontains=search) |
                Q(address__icontains=search) |
                Q(city__icontains=search)
            )
        if city:
            queryset = queryset.filter(city__icontains=city)
        return queryset
    

class CardListAPIView(generics.ListAPIView):
    queryset = Card.objects.all()
    serializer_class = CardListSerializer
    pagination_class = CustomPagination

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name='cat_id',
                description='Фильтр по ID категории',
                required=False,
                type=int,
                location=OpenApiParameter.QUERY,
                examples=[
                    OpenApiExample(
                        "Фильтр по категории с ID 1",
                        value=1,
                        summary="cat_id=1"
                    ),
                    OpenApiExample(
                        "Фильтр по категории с ID 3",
                        value=3,
                        summary="cat_id=3"
                    ),
                ],
            ),
        ],
        description=(
            "Примеры запросов:\n"
            "- /api/cards/\n"
            "- /api/cards/?cat_id=1\n"
            "- /api/cards/?cat_id=3\n"
        ),
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        cat_id = self.request.query_params.get('cat_id')

        if cat_id:
            queryset = queryset.filter(category__id=cat_id)

        return queryset
    

class TypesByCategoryAPIView(ListAPIView):
    serializer_class = TypeSerializer

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name='cat_id',
                description='ID категории, например: Еда, Спорт и т.д.',
                required=True,
                type=int,
                location=OpenApiParameter.QUERY,
                examples=[
                    OpenApiExample("Еда", value=1, summary="cat_id=1"),
                    OpenApiExample("Спорт", value=2, summary="cat_id=2"),
                ],
            )
        ],
        description="Возвращает все типы карточек (например, Чайхана, Кафе и т.д.) по категории.",
        responses=TypeSerializer(many=True),
    )
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def get_queryset(self):
        cat_id = self.request.query_params.get("cat_id")
        if not cat_id:
            raise ValidationError({"cat_id": "Этот параметр обязателен."})
        return Type.objects.filter(cards__category__id=cat_id).distinct()


class CardsByTypeAPIView(ListAPIView):
    serializer_class = CardListSerializer
    pagination_class = CustomPagination

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name='cat_id',
                description='ID категории (например: Еда, Спорт)',
                required=True,
                type=int,
                location=OpenApiParameter.QUERY,
            ),
            OpenApiParameter(
                name='type_id',
                description='ID типа (например: Чайхана, Кафе)',
                required=True,
                type=int,
                location=OpenApiParameter.QUERY,
            ),
        ],
        description="Возвращает карточки, относящиеся к категории и типу.",
        responses=CardListSerializer(many=True),
    )
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def get_queryset(self):
        cat_id = self.request.query_params.get("cat_id")
        type_id = self.request.query_params.get("type_id")

        if not cat_id or not type_id:
            raise ValidationError("Параметры cat_id и type_id обязательны.")

        return Card.objects.filter(category__id=cat_id, type__id=type_id)