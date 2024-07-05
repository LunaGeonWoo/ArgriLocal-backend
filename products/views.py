from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product
from .serializers import ProductTinySerializer


class Products(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductTinySerializer(products, many=True)
        return Response(serializer.data)
