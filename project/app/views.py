from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializerls import SignUpSerializer, LoginSerializer
from .models import SignUp, Login

"""
API Overview
"""


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'sign-up': '/sign-up/',
        'login': '/login/',
    }
    return Response(api_urls)


@api_view(['POST'])
def signUp(request):
    serializer = SignUpSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(["POST"])
def login(request):
    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.data["username"]
        pwd = serializer.data["password"]
        try:
            details = SignUp.objects.get(username=user, password=pwd)
            serializers = SignUpSerializer(details, many=False)
            return Response(serializers.data)
        except:
            error = {
                "error": "You entered wrong credentials"
            }
            return Response(error)
