from rest_framework import serializers
from apps.cards.models.card import Card
from apps.reviews.models.review import Review

class CardWithReviewSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    avg_rating = serializers.FloatField()

    class Meta:
        model = Card
        fields = ['id', 'title', 'category', 'address', 'avg_rating']