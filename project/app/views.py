import jwt
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializerls import UserSerializer, LoginSerializer, UserProfileSerializer
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
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def getProfile(request):
    decodedPayload = jwt.decode(request.headers["authorization"].split()[1], algorithms=['HS512'],
                                key='django-insecure-ccy8d&94ym$t^wa4_6dx2!+u#!v=)@1g7)4lob9z8=o!trzg98')
    user = CustomUser.objects.get(id=decodedPayload["user_id"])
    customserializer = UserSerializer(user, many=False)
    userrole = customserializer.data["role"]
    if userrole == "A":
        user = UserProfile.objects.all()
        serializer = UserProfileSerializer(user, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)


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
        }
        )
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateProfile(request):
    user = request.user
    serializer = UserProfileSerializer(user, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
