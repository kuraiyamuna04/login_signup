from rest_framework import status
from rest_framework.generics import *
from rest_framework.permissions import IsAuthenticated, BasePermission, SAFE_METHODS
from rest_framework.response import Response
from .serializerls import UserSerializer, LoginSerializer, UserProfileSerializer
from .models import *
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView


class RequiredAdmin(BasePermission):
    def has_permission(self, request, view):
        user = request.user.role
        try:
            if str(user) == 'A':
                return Response({})
        except Exception as e:
            print(e)


class RequiredManager(BasePermission):
    def has_permission(self, request, view):
        user = request.user.role
        try:
            if str(user) == 'M':
                return Response({})
        except Exception as e:
            print(e)


class RequiredEmployee(BasePermission):
    def has_permission(self, request, view):
        role = request.POST.get("role")
        try:
            if str(role) == 'E':
                return Response({})
        except Exception as e:
            print(e)


class AdminCanCreate(BasePermission):
    def has_permission(self, request, view):
        role = request.POST.get("role")
        try:
            if str(role) == 'M' or str(role) == 'E':
                return Response({})
        except Exception as e:
            print(e)


class ManagerCanCreate(BasePermission):
    def has_permission(self, request, view):
        role = request.POST.get("role")
        try:
            if str(role) == 'E':
                return Response({})
        except Exception as e:
            print(e)


class SignUpView(CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class ProfileSignUpView(CreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user_role = request.user.role
        user_id = request.user.id
        if user_role == "A":
            user = UserProfile.objects.all()
            serializer = UserProfileSerializer(user, many=True)
            return Response(serializer.data)
        else:
            user = UserProfile.objects.get(user=user_id)
            serializer = UserProfileSerializer(user)
            return Response(serializer.data)

    def put(self, request):
        user_id = request.user.id
        user_profile = UserProfile.objects.get(user_id=user_id)
        profile_serializer = UserProfileSerializer(instance=user_profile, data=request.data)

        if not profile_serializer.is_valid():
            return Response(status=status.HTTP_404_NOT_FOUND)
        profile_serializer.save()
        return Response(profile_serializer.data)


class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        password = serializer.initial_data["password"]
        phone = serializer.initial_data["phone_number"]
        print(phone, password)
        user = authenticate(request, phone_number=phone, password=password)
        print(user)
        if not user:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        Refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(Refresh),
            "access": str(Refresh.access_token)
        }
        )


class AdminAccessView(ListAPIView, CreateAPIView):
    permission_classes = [IsAuthenticated, RequiredAdmin]

    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class UpdateProfileView(APIView):
    permission_classes = [IsAuthenticated, RequiredAdmin]

    def put(self, request, pk):
        user_profile = UserProfile.objects.get(user_id=pk)
        profile_serializer = UserProfileSerializer(instance=user_profile, data=request.data)

        if not profile_serializer.is_valid():
            return Response(status=status.HTTP_404_NOT_FOUND)
        profile_serializer.save()
        return Response(profile_serializer.data)


class AdminAddUserView(APIView):
    permission_classes = [IsAuthenticated, RequiredAdmin, AdminCanCreate]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer.save()
        email = request.POST.get("email")
        user = CustomUser.objects.get(email=email)
        user.is_active = True
        user.save()
        return Response(serializer.data)


class ManagerAddUserView(APIView):
    permission_classes = [IsAuthenticated, RequiredManager, ManagerCanCreate]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer.save()
        email = request.POST.get("email")
        user = CustomUser.objects.get(email=email)
        user.is_active = True
        user.save()
        return Response(serializer.data)


class AdminAddProfile(CreateAPIView):
    permission_classes = [IsAuthenticated, RequiredAdmin]

    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class ManagerAddProfile(CreateAPIView):
    permission_classes = [IsAuthenticated, RequiredManager, RequiredEmployee]

    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
