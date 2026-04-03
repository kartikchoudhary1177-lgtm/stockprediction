from user_auth.models import User
from rest_framework import serializers
from django.contrib.auth.hashers import make_password


class Userseri(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username",'password',"email","role"]
   
    def validate_email(self, value):
        
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already exists")
        return value
        
    def create(self,value):
        
        value["password"]=make_password(value["password"])
        return super().create(value)
