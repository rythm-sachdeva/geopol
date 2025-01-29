from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from chat.serializers import GetUserSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


# Create your views here.
User = get_user_model()

class GET_USER_VIEW(APIView):
    def get(self,request):
        try:
            users = User.objects.all()
            serializer = GetUserSerializer(users, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            print("Error in getting user list", str(e))
            return Response({"error":"Error In Getting The User List "}, status=status.HTTP_400_BAD_REQUEST)
    
class GetUserDetails(APIView):
    permission_classes = [IsAuthenticated]
    
    
    def get(self,request):
        try:
            user = request.user
            serializer = GetUserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            print("Error in getting user details", str(e))
            return Response({"error":"Error In Getting The User Details "}, status=status.HTTP_400_BAD_REQUEST)
        


        

