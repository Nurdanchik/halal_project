from django.urls import path
from .views.card import TestCacheView

urlpatterns = [
    path('test-cache/', TestCacheView.as_view(), name='test-cache'),
]