from django.urls import path
from apps.cards.views.featured_card_view import FeaturedCardListView
from apps.cards.views.card_food_view import FoodCardListView
from apps.cards.views.card_full_info import CardFullInfoView
from apps.cards.views.other_app_views import (
    ReligionCardsView, ServicesCardsView, BusinessCardsView, FamilyCardsView
)

urlpatterns = [
    path('api/featured-cards/', FeaturedCardListView.as_view(), name='featured-cards-list'),
    path('food/', FoodCardListView.as_view(), name='food-card-list'),
    path('religion/', ReligionCardsView.as_view()),
    path('services/', ServicesCardsView.as_view()),
    path('business/', BusinessCardsView.as_view()),
    path('family/', FamilyCardsView.as_view()),
    path('full-info/<int:pk>/', CardFullInfoView.as_view(), name='card-full-info'),
]