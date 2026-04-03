from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import StockAlert
from .serializers import StockAlertSerializer

class CreateStockAlertView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = StockAlertSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(
                {
                    "message": "Alert created successfully",
                    "data": serializer.data
                },
                status=status.HTTP_201_CREATED
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)