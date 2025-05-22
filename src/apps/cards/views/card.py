from rest_framework.generics import RetrieveAPIView
from apps.cards.models.card import Card
from apps.cards.serializers.card_full_info_serializers import CardFullInfoSerializer
from common.pagination import CustomPagination
from rest_framework.generics import ListAPIView
from apps.cards.models.card import Card
from apps.cards.models.featured_card import FeaturedCard
from apps.cards.serializers.card_serializers import CardListSerializer
from apps.cards.serializers.featured_card_serializers import FeaturedCardListSerializer
from apps.cards.services.card_service import get_all_cards
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema, OpenApiParameter
    

from rest_framework.generics import RetrieveAPIView
from apps.cards.models.card import Card
from apps.cards.serializers.card_full_info_serializers import CardFullInfoSerializer

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
    

class CardListAPIView(ListAPIView):
    serializer_class = CardListSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category']  
    pagination_class = CustomPagination

    def get_queryset(self):
        return get_all_cards()