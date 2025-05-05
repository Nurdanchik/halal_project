from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin

from .models.card import Card
from .models.location import Place
from .models.featured_card import FeaturedCard


@admin.register(Place)
class PlaceAdmin(OSMGeoAdmin):  # ← теперь карта OSM (OpenStreetMap)
    list_display = ('id', 'name')
    search_fields = ('name',)


class FeaturedCardInline(admin.TabularInline):
    model = FeaturedCard
    extra = 1


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', 'category', 'location')
    search_fields = ('description',)
    list_filter = ('category',)
    inlines = [FeaturedCardInline]