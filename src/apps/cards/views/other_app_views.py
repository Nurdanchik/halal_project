from rest_framework.generics import ListAPIView
from apps.cards.serializers.other_app_serializers import CardWithReviewSerializer
from apps.cards.services.other_app_services import get_religion_cards, get_services_cards, get_business_cards, get_family_cards
from common.pagination import CustomPagination


class ReligionCardsView(ListAPIView):
    serializer_class = CardWithReviewSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        return get_religion_cards()

class ServicesCardsView(ListAPIView):
    serializer_class = CardWithReviewSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        return get_services_cards()

class BusinessCardsView(ListAPIView):
    serializer_class = CardWithReviewSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        return get_business_cards()

class FamilyCardsView(ListAPIView):
    serializer_class = CardWithReviewSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        return get_family_cards()