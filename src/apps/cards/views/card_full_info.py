from rest_framework.generics import RetrieveAPIView
from apps.cards.models.card import Card
from apps.cards.serializers.card_full_info import CardFullInfoSerializer

class CardFullInfoView(RetrieveAPIView):
    queryset = Card.objects.all()
    serializer_class = CardFullInfoSerializer