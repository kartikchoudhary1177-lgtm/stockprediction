import requests
from django.conf import settings


def get_alpha_stock(symbol):
    url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={settings.ALPHA_VANTAGE_KEY}"

    try:
        r = requests.get(url, timeout=10)
        data = r.json()
        quote = data["Global Quote"]

        return {
            "symbol": quote["01. symbol"],
            "price": float(quote["05. price"]),
            "high": float(quote["03. high"]),
            "low": float(quote["04. low"]),
            "volume": quote["06. volume"],
            "source": "Alpha Vantage"
        }
    except:
        return None


def get_finnhub_stock(symbol):
    url = f"https://finnhub.io/api/v1/quote?symbol={symbol}&token={settings.FINNHUB_KEY}"

    try:
        r = requests.get(url, timeout=10)
        data = r.json()

        return {
            "symbol": symbol.upper(),
            "price": float(data["c"]),
            "high": float(data["h"]),
            "low": float(data["l"]),
            "source": "Finnhub"
        }
    except:
        return None


def get_stockdata_stock(symbol):
    url = f"https://api.stockdata.org/v1/data/quote?symbols={symbol}&api_token={settings.STOCKDATA_KEY}"

    try:
        r = requests.get(url, timeout=10)
        data = r.json()
        stock = data["data"][0]

        return {
            "symbol": stock["ticker"],
            "price": float(stock["price"]),
            "high": float(stock["day_high"]),
            "low": float(stock["day_low"]),
            "source": "StockData"
        }
    except:
        return None


def get_combined_stock(symbol):
    data = get_alpha_stock(symbol)
    if data:  
        return data

    data = get_finnhub_stock(symbol)
    if data:
        return data

    data = get_stockdata_stock(symbol)
    return data
    


def get_live_stock_price(symbol):
    stock = get_combined_stock(symbol)

    if stock:
        return stock["price"]

    return None


def get_stock_range(symbol, start_date, end_date):
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={settings.ALPHA_VANTAGE_KEY}"

    try:
        r = requests.get(url, timeout=10)
        data = r.json()
        series = data["Time Series (Daily)"]

        result = []

        for date, values in series.items():
            if start_date <= date <= end_date:
                result.append({
                    "date": date,
                    "open": values["1. open"],
                    "high": values["2. high"],
                    "low": values["3. low"],
                    "close": values["4. close"],
                    "volume": values["5. volume"]
                })

        return {
            "symbol": symbol.upper(),
            "start_date": start_date,
            "end_date": end_date,
            "data": result
        }
    except:
        return None
    
def get_stock_price(symbol):
    data = get_combined_stock(symbol)
    if not data:
        return None
    return data.get("price")