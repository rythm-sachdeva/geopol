import jwt
from jwt import InvalidTokenError, ExpiredSignatureError
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.conf import settings
from django.contrib.auth import get_user_model
from datetime import datetime,timedelta
from channels.db import database_sync_to_async

User = get_user_model()

class JWTAuthentication(BaseAuthentication):

    def authenticate(self,request):
        token = self.extract_token(request)
        if token is None:
            return None
        
        try:
            payload = jwt.decode(token,settings.SECRET_KEY,algorithms=['HS256'])
            user_id = payload.get('id')
            user = User.objects.get(id=user_id)
            return user
        except (InvalidTokenError,ExpiredSignatureError,User.DoesNotExist):
            raise AuthenticationFailed("Invalid Token")



    def verify_token(self,payload):
        if "exp" not in payload:
            raise InvalidTokenError("Token is missing expiration time")
        expiration = payload['exp']
        current_time = datetime.utcnow().timestamp()
        if current_time>expiration:
            raise ExpiredSignatureError("Token has expired")
    
    @database_sync_to_async
    def authenticate_websocket(self,scope,token):
        try:
            payload = jwt.decode(token,settings.SECRET_KEY,algorithms=['HS256'])
            user_id = payload.get('id')
            user = User.objects.get(id=user_id)
            return user
        except (InvalidTokenError,ExpiredSignatureError,User.DoesNotExist):
            raise AuthenticationFailed("Invalid Token")

        

    def extract_token(self,request):
        auth_header = request.headers.get('Authorization',None)
        if auth_header and auth_header.startswith('Bearer'):
            return auth_header.split(" ")[1]
        return None

    @staticmethod
    def generate_token(payload):
        expiration = datetime.utcnow() + timedelta(hours=24)
        payload['exp'] = expiration
        token = jwt.encode(payload,settings.SECRET_KEY,algorithm='HS256')
        return token
    

