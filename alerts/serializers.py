from rest_framework import serializers
from .models import StockAlert

class StockAlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockAlert
        fields = "__all__"
        read_only_fields = ["user", "is_triggered", "created_at"]