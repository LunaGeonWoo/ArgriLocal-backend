from django.urls import path
from .views import Products, ProductDetail

urlpatterns = [
    path("", Products.as_view()),
    path("<int:id>/", ProductDetail.as_view()),
]
