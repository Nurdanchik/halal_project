from rest_framework import serializers
from apps.cards.models.card import Card, CardPhoto, CardVideo
from apps.reviews.serializers.review import ReviewSerializer
from common.pagination import CustomPagination


class CardPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CardPhoto
        fields = ['id', 'image']


class CardVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CardVideo
        fields = ['id', 'video']


class CardFullInfoSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    type = serializers.StringRelatedField()
    location = serializers.SerializerMethodField()
    photos = CardPhotoSerializer(many=True, read_only=True)
    videos = CardVideoSerializer(many=True, read_only=True)
    reviews = serializers.SerializerMethodField()
    face_img = serializers.ImageField()
    
    class Meta:
        model = Card
        fields = [
            'id', 'title', 'face_img', 'category', 'type', 'description',
            'phone_number', 'whatsapp', 'telegram', 'site',
            'start_work', 'stops_work', 'work_days', 'location',
            'address', 'city', 'video', 'photos', 'videos', 'reviews'
        ]

    def get_location(self, obj):
        if obj.location:
            return {
                'name': obj.location.name,
                'latitude': obj.location.latitude,
                'longitude': obj.location.longitude
            }
        return None

    def get_reviews(self, obj):
        """
        Пагинируем и фильтруем отзывы к карточке
        """
        request = self.context.get('request')
        reviews_qs = obj.reviews.filter(is_approved=True).order_by('-created_at')

        paginator = CustomPagination()
        paginator.page_size = 5
        paginated_reviews = paginator.paginate_queryset(reviews_qs, request)

        serializer = ReviewSerializer(paginated_reviews, many=True, context={'request': request})
        return paginator.get_paginated_response(serializer.data).data
