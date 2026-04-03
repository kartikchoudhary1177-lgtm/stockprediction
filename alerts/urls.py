from django.urls import path
from .views import CreateStockAlertView

urlpatterns = [
    path("create/", CreateStockAlertView.as_view(), name="create-stock-alert"),
]