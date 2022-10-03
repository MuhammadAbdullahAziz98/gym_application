from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated , AllowAny
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenViewBase
from rest_framework import generics
from django.contrib.auth import get_user_model
from .serializers import RegisterSerializer
from .serializers import UserSerializer

UserModel = get_user_model()
# Create your views here.

class HelloView(APIView):
    permission_classes = (IsAuthenticated,)             

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)

class TokenObtainUserSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        data["token"] = {"access": data["access"], "refresh": data["refresh"]}
        del data["access"]
        del data["refresh"]
        data["user"] = UserSerializer(self.user).data
        return data


class TokenObtainUserView(TokenViewBase):

    serializer_class = TokenObtainUserSerializer


class RegisterView(generics.CreateAPIView):
    queryset = UserModel.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer