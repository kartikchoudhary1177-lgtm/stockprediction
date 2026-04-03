from rest_framework.views import APIView
from rest_framework.response import Response

from .services import get_combined_stock,get_stock_range
from .chatbot import stock_chatbot
from rest_framework.permissions import IsAuthenticated


class StockAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):

        symbol = request.GET.get("symbol")

        if not symbol:
            return Response({"error": "symbol required"})

        stock = get_combined_stock(symbol)

        if not stock:
            return Response({"error": "stock not found"})

        return Response({
            "symbol": symbol.upper(),
            "current_price": stock.get("price"),
            "high_price": stock.get("high"),
            "low_price": stock.get("low"),
            "volume": stock.get("volume"),
            "data_source": stock.get("source")
        })
class ChatbotAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):

        symbol = request.GET.get("symbol")
        question = request.GET.get("question")

        stock = get_combined_stock(symbol)

        if not stock:
            return Response({"error": "stock not found"})

        answer = stock_chatbot(stock, question)

        return Response({
            "symbol": symbol.upper(),
            "question": question,
            "answer": answer
        })


class StockHistoryAPIView(APIView):
    
    permission_classes = [IsAuthenticated]
    def get(self, request):

        symbol = request.GET.get("symbol")
        start_date = request.GET.get("start_date")
        end_date = request.GET.get("end_date")

        if not symbol or not start_date or not end_date:
            return Response({
                "error": "symbol, start_date and end_date required"
            })

        data = get_stock_range(symbol, start_date, end_date)

        if not data:
            return Response({
                "error": "data not found"
            })

        return Response(data)