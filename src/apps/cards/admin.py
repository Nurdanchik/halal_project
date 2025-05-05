from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin

from .models.card import Card, CardPhoto
from .models.featured_card import FeaturedCard
from .models.location import Place
from .models.featured_card import FeaturedCard


@admin.register(Place)
class PlaceAdmin(LeafletGeoAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


class FeaturedCardInline(admin.TabularInline):
    model = FeaturedCard
    extra = 1


class CardPhotoInline(admin.TabularInline):
    model = CardPhoto
    extra = 1

@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    inlines = [CardPhotoInline]
    list_display = ('description', 'category', 'start_work', 'stops_work')

admin.site.register(CardPhoto)
admin.site.register(FeaturedCard)