from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        password = validated_data.pop('password', None)  # Remove password before passing data
        user = get_user_model().objects.create_user(**validated_data)  # Create user

        if password:
            user.set_password(password)  
            user.save()

        return user  

    class Meta:
        model = get_user_model()
        fields = ['id', 'email', 'password', 'first_name', 'last_name']  # ✅ Include 'id'
        extra_kwargs = {'password': {'write_only': True}}

class LoginSerialiser(serializers.Serializer):
    email = serializers.EmailField()
    id = serializers.CharField(max_length=15,read_only=True)
    password = serializers.CharField(max_length=255,write_only=True)

    def validate(self, data):
        email = data.get('email',None)
        password = data.get('password',None)

        if(email is None):
            raise serializers.ValidationError("An email address is required to log in.")
        if(password is None):
            raise serializers.ValidationError("A password is required to log in.")
        
        user = authenticate(email=email,password=password)
        if user is None:
            raise serializers.ValidationError("Invalid Email or Password")
        

        return {
            'email':user.email,
            'id':user.id
        }

