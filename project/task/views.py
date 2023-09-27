from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from app.models import UserProfile, CustomUser
from utils.decorators import RequiredManager
from .serializers import CreateTaskSerializers
from utils.helper import check_post_req_role


class CreateTaskView(APIView):
    permission_classes = [IsAuthenticated, RequiredManager]

    def post(self, request):
        serializer = CreateTaskSerializers(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        try:
            user_id = request.data["assigned_to"]
            print(user_id)
            if not check_post_req_role(user_id):
                return Response(
                    {"msg": "You Don't Have Permission To Add This"}, status=status.HTTP_401_UNAUTHORIZED
                )
            user_name = request.user.userProfiles
            serializer.validated_data["assigned_by"] = user_name
            serializer.save()
            return Response(serializer.data)
        except Exception:
            return Response({"msg:You entered wrong data"}, status.HTTP_400_BAD_REQUEST)
