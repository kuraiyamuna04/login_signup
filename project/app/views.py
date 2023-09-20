from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializerls import CustomUserSerializer
from .models import CustomUser
from django.contrib.auth.hashers import check_password
from django.core.exceptions import ObjectDoesNotExist


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'sign-up': '/sign-up/',
        'login': '/login/',
    }
    return Response(api_urls)


@api_view(['POST'])
def signUp(request):
    serializer = CustomUserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def login(request):
    serializer = CustomUserSerializer(data=request.data)
    if serializer.is_valid():
        pwd = serializer.data["password"]
        user = serializer.data["username"]
        email = serializer.data["email"]
        try:
            details = CustomUser.objects.get(username=user, email=email)
            serializers = CustomUserSerializer(details, many=False)
            if check_password(pwd, serializers.data["password"]):
                return Response(status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_401_UNAUTHORIZED)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)
