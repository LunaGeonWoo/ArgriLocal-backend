from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import exceptions
from .models import Product
from .serializers import ProductTinySerializer, ProductDetailSerializer


class Products(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductTinySerializer(products, many=True)
        return Response(serializer.data)


class ProductDetail(APIView):
    def get_object(self, id):
        try:
            return Product.objects.get(id=id)
        except:
            raise exceptions.NotFound

    def get(self, request, id):
        product = self.get_object(id)
        serializer = ProductDetailSerializer(product)
        return Response(serializer.data)
