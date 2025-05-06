from rest_framework.generics import ListAPIView
from apps.cards.serializers.card_food_serializer import CardFoodSerializer
from apps.cards.services.card_food_service import get_food_cards
from common.pagination import CustomPagination


class FoodCardListView(ListAPIView):
    serializer_class = CardFoodSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        return get_food_cards()