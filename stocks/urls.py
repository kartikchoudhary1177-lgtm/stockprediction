from django.urls import path
from .views import StockAPIView,ChatbotAPIView,StockHistoryAPIView

urlpatterns = [
    path("stock/", StockAPIView.as_view(), name="stock-api"),
    path("chatbot/", ChatbotAPIView.as_view()),
    path("stock_history/", StockHistoryAPIView.as_view())
    
]