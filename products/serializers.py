from rest_framework import serializers
from .models import Product


class ProductTinySerializer(serializers.ModelSerializer):
    producer = serializers.SerializerMethodField()
    address = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = (
            "id",
            "producer",
            "address",
            "name",
            "image_url",
            "price",
            "created_at",
        )

    def get_producer(self, product):
        return product.owner.name

    def get_address(self, product):
        return product.owner.address
