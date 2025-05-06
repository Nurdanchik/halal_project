from rest_framework import serializers
from apps.cards.models.card import Card, CardPhoto
from apps.reviews.models.review import Review


class CardPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CardPhoto
        fields = ['id', 'image']


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'author', 'review', 'stars']


class CardFullInfoSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    type = serializers.CharField(source='get_type_display')
    location = serializers.SerializerMethodField()
    photos = CardPhotoSerializer(many=True, source='photos.all')
    reviews = serializers.SerializerMethodField()

    class Meta:
        model = Card
        fields = [
            'id', 'title', 'category', 'type', 'description',
            'phone_number', 'whatsapp', 'telegram', 'site',
            'start_work', 'stops_work', 'work_days', 'location',
            'address',  # <-- добавляем сюда адрес прямо из Card
            'video', 'photos', 'reviews'
        ]

    def get_location(self, obj):
        if obj.location:
            return {
                'latitude': obj.location.latitude,
                'longitude': obj.location.longitude
            }
        return None

    def get_reviews(self, obj):
        request = self.context.get('request')
        reviews_qs = obj.reviews.filter(is_approved=True).order_by('-created_at')

        from rest_framework.pagination import PageNumberPagination
        paginator = PageNumberPagination()
        paginator.page_size = 5
        paginated_reviews = paginator.paginate_queryset(reviews_qs, request)

        serializer = ReviewSerializer(paginated_reviews, many=True, context={'request': request})
        return paginator.get_paginated_response(serializer.data).data