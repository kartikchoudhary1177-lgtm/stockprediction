from django.shortcuts import render
from user_auth.models import User
from user_auth.serializers import Userseri
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.hashers import check_password 
from rest_framework_simplejwt.tokens import RefreshToken
from django.db.models import Q

# Create your views here.

class Userview(APIView):
    def post(self,request):
        seri = Userseri(data=request.data)
        if seri.is_valid():
            seri.save()
            return Response({
    "message": "you are registered successfully",
    "data": {
        "username": seri.data["username"],
        "email": seri.data["email"]
    }
})
        
        return Response(seri.errors)
class Login(APIView):
    def post(self,request):
        username= request.data.get("username")
        password=request.data.get('password')
        email=request.data.get('email')
        
        try:
            user = User.objects.get(Q(username=username) | Q(email=email))
        except User.DoesNotExist:
            return Response({"error": "User not found"})
            
        if not user.check_password(password):
            return Response("wrong password")
        refresh = RefreshToken.for_user(user)
        
        return Response({
    "user": {
        "id": user.id,
        "username": user.username,
    },
    "access_token": str(refresh.access_token),
    "refresh_token": str(refresh)
})