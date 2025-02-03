from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from chat.serializers import GetUserSerializer, ChatSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from chat.models import ChatModel
from django.db.models import Q


# Create your views here.
User = get_user_model()

class GET_USER_VIEW(APIView):
    # permission_classes = [IsAuthenticated]
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

class GetSenderMessages(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self,request,id,*args,**kwargs):
        try:
            sender = User.objects.get(id=id)
            user = request.user
            sender_messages = ChatModel.objects.filter(
    Q(sender=sender, reciever=user) | Q(sender=user, reciever=sender)
).order_by("time_stamp")

            serializer = ChatSerializer(sender_messages, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            print("Error in getting sender messages", str(e))
            return Response({"error":"Error In Getting The Sender Messages "}, status=status.HTTP_400_BAD_REQUEST)


        

