from rest_framework import serializers
from apps.cards.models.featured_card import FeaturedCard
from apps.cards.models.card import Card


class CardSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()  

    class Meta:
        model = Card
        fields = ['id', 'title', 'category']

class FeaturedCardSerializer(serializers.ModelSerializer):
    card = CardSerializer(read_only=True)

    class Meta:
        model = FeaturedCard
        fields = ['id', 'card']