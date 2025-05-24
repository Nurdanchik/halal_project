from django.contrib import admin


from .models.card import Card, CardPhoto, CardVideo
from .models.featured_card import FeaturedCard
from .models.location import Place
from .models.type import Type


admin.site.register(Place)


class FeaturedCardInline(admin.TabularInline):
    model = FeaturedCard
    extra = 1


class CardPhotoInline(admin.TabularInline):
    model = CardPhoto
    extra = 3 


admin.site.register(Type)
admin.site.register(CardVideo)

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