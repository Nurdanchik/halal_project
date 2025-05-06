from apps.cards.models.card import Card
from django.db.models import Avg, Q

def get_cards_by_type(card_type):
    return Card.objects.filter(type=card_type).annotate(
        avg_rating=Avg('reviews__stars', filter=Q(reviews__is_approved=True))
    )

def get_religion_cards():
    return get_cards_by_type('religion')

def get_services_cards():
    return get_cards_by_type('services')

def get_business_cards():
    return get_cards_by_type('business')

def get_family_cards():
    return get_cards_by_type('family')