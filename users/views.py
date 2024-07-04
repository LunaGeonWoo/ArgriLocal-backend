from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import exceptions, status
from django.contrib.auth import login
from .serializers import PrivateUserSerializer
from .models import User


class Users(APIView):
    def post(self, request):
        password = request.data.get("password")
        if not password:
            raise exceptions.ParseError
        serializer = PrivateUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(password)
            user.save()
            serializer = PrivateUserSerializer(user)
            login(request, user)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class UserName(APIView):
    def get(self, request, username):
        if User.objects.filter(username=username).exists():
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_200_OK)
