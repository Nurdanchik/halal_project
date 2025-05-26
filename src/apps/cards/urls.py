from django.urls import path
from apps.cards.views.card import CardDetailView, CardSearcherListAPIView, FeaturedCardListAPIView, CardListAPIView


urlpatterns = [
    path('details/<int:pk>/', CardDetailView.as_view(), name='card-full-info'),
    path('searcher', CardSearcherListAPIView.as_view(), name='card-search'),
    path('', CardListAPIView.as_view(), name='card-list'),
    path('featured', FeaturedCardListAPIView.as_view(), name='featured-card-list'),
]