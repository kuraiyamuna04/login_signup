from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from app.models import UserProfile, CustomUser
from utils.decorators import RequiredManager
from .serializers import CreateTaskSerializers


class CreateTaskView(APIView):
    permission_classes = [IsAuthenticated, RequiredManager]

    def post(self, request):
        serializer = CreateTaskSerializers(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        try:
            user_id= request.POST.get["assigned_to"]
            user = CustomUser.objects.get(id=user_id)
            role = user.role
            if role != "E":
                return Response(
                    {"msg": "You Don't Have Permission To Access This"}, status=status.HTTP_401_UNAUTHORIZED
                )
            user = request.user
            userprofile = UserProfile.objects.get(user_id=user)
            serializer.validated_data["assigned_by"] = userprofile.first_name
            serializer.save()
            return Response(serializer.data)
        except:
            return Response({"msg:You entered wrong data"}, status.HTTP_400_BAD_REQUEST)
