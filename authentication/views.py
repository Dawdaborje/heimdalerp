from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from knox.views import LoginView as KnoxLoginView
from .serializers import UserAuthSerializer, UserRegisterSerializer
from rest_framework.permissions import AllowAny
from django.contrib.auth import login

# Create your views here.


class UserRegisteration(APIView):
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(KnoxLoginView):
    permission_classes = (AllowAny)

    def post(self, request, format=None):
        serializer = UserAuthSerializer, UserRegisterSerializer(
            data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginView, self).post(request, format=None)
