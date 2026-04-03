import yfinance as yf

def get_previous_stock_data(symbol):
    ticker = yf.Ticker(symbol)
    hist = ticker.history(period="7d")

    if hist.empty:
        return None

    closes = hist["Close"].tolist()

    return {
        "previous_close": round(closes[-2], 2) if len(closes) > 1 else round(closes[-1], 2),
        "latest_close": round(closes[-1], 2),
        "5_day_avg": round(sum(closes[-5:]) / min(len(closes), 5), 2),
        "trend": "UP" if closes[-1] > closes[0] else "DOWN"
    }