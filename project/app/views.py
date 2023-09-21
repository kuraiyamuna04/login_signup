from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializerls import UserSerializer, LoginSerializer
from .models import *
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'sign-up': '/sign-up/',
        'login': '/login/',
    }
    return Response(api_urls)


@api_view(['POST'])
def signUp(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():  # find how we can ignore if and else here.
        serializer.save()
        return Response(status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def login(request):
    serializer = LoginSerializer(data=request.data)
    password = serializer.initial_data["password"]
    phone = serializer.initial_data["phone_number"]
    user = authenticate(request, phone_number=phone, password=password)
    if user:
        Refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(Refresh),
            "access": str(Refresh.access_token)
        })
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)


@api_view(['GET'])
def view(request):
    users = CustomUser.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)
