from rest_framework import serializers
from apps.cards.models.featured_card import FeaturedCard

class FeaturedCardListSerializer(serializers.ModelSerializer):
    card_id = serializers.IntegerField(source='card.id')

    class Meta:
        model = FeaturedCard
        fields = ['id', 'card_id']