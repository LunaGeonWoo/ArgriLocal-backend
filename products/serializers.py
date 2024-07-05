from rest_framework import serializers
from .models import Product
from users.serializers import PublicUserSerializer


class ProductTinySerializer(serializers.ModelSerializer):
    owner = serializers.SerializerMethodField()
    address = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = (
            "id",
            "owner",
            "address",
            "name",
            "image_url",
            "price",
            "created_at",
        )

    def get_owner(self, product):
        return product.owner.name

    def get_address(self, product):
        return product.owner.address


class ProductDetailSerializer(serializers.ModelSerializer):
    owner = PublicUserSerializer()

    class Meta:
        model = Product
        fields = (
            "id",
            "owner",
            "name",
            "image_url",
            "description",
            "price",
            "created_at",
        )
