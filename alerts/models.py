from django.db import models
from django.conf import settings

class StockAlert(models.Model):
    ALERT_CHOICES = [
        ("below", "Below"),
        ("above", "Above"),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    symbol = models.CharField(max_length=20)
    target_price = models.FloatField()
    email = models.EmailField()
    alert_type = models.CharField(max_length=10, choices=ALERT_CHOICES, default="below")
    is_active = models.BooleanField(default=True)
    is_triggered = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.symbol} - {self.alert_type} - {self.target_price}"