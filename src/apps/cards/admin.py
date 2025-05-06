from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin

from .models.card import Card, CardPhoto
from .models.featured_card import FeaturedCard
from .models.location import Place


@admin.register(Place)
class PlaceAdmin(LeafletGeoAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


class FeaturedCardInline(admin.TabularInline):
    model = FeaturedCard
    extra = 1


class CardPhotoInline(admin.TabularInline):
    model = CardPhoto
    extra = 3 


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    inlines = [CardPhotoInline, FeaturedCardInline]  
    list_display = ('id', 'title', 'category', 'phone_number') 
    search_fields = ('title', 'description')


@admin.register(CardPhoto)
class CardPhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'card', 'image')
    search_fields = ('card__title',)


@admin.register(FeaturedCard)
class FeaturedCardAdmin(admin.ModelAdmin):
    list_display = ('id', 'card')
    search_fields = ('card__title',)