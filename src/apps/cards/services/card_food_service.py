from apps.cards.models.card import Card

def get_food_cards():
    return Card.objects.filter(type='food')