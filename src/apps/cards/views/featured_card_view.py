from rest_framework.views import APIView
from rest_framework.response import Response
from apps.cards.serializers.featured_card_serializers import FeaturedCardSerializer
from apps.cards.services.featured_card_service import get_all_featured_cards
from common.pagination import CustomPagination


class FeaturedCardListView(APIView):
    pagination_class = CustomPagination
    
    def get(self, request):
        featured_cards = get_all_featured_cards()
        serializer = FeaturedCardSerializer(featured_cards, many=True)
        return Response(serializer.data)