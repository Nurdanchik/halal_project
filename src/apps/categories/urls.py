from django.urls import path
from apps.categories.views.category import CategoryListAPIView

urlpatterns = [
    path('', CategoryListAPIView.as_view(), name='category-list'),
]