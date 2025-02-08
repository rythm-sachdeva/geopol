from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer,LoginSerialiser
from rest_framework import status
from .tokenAuthentication import JWTAuthentication

# Create your views here.
class RegisterView(APIView):
    
    def post(self,request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            token = JWTAuthentication.generate_token(serializer.validated_data)
            return Response({'message':'registration Successfull'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):

    def post(self,request):
        serializers = LoginSerialiser(data=request.data)
        if serializers.is_valid():
            token = JWTAuthentication.generate_token(serializers.validated_data)
            return Response({'message':'Login Successfull','token':token,'user':serializers.data},status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

    
