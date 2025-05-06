from rest_framework import serializers
from apps.cards.models.card import Card
from apps.reviews.services.review_service import get_average_rating_for_card

class CardFoodSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Card
        fields = ['id', 'title', 'category', 'address', 'average_rating']

    def get_average_rating(self, obj):
        return get_average_rating_for_card(obj)