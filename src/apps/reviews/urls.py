from django.urls import path
from apps.reviews.views.review import ReviewCreateView

urlpatterns = [
    path('create/', ReviewCreateView.as_view(), name='review-create'),
]