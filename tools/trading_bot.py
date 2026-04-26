import yfinance as yf

# Simple Moving Average Strategy

def get_data(stock):
    data = yf.download(stock, period="1mo", interval="1d")
    return data

def calculate_signals(data):
    data['SMA_5'] = data['Close'].rolling(window=5).mean()
    data['SMA_10'] = data['Close'].rolling(window=10).mean()

    if data['SMA_5'].iloc[-1] > data['SMA_10'].iloc[-1]:
        return "BUY"
    elif data['SMA_5'].iloc[-1] < data['SMA_10'].iloc[-1]:
        return "SELL"
    else:
        return "HOLD"

def run_bot(stock):
    data = get_data(stock)
    signal = calculate_signals(data)

    print(f"\nStock: {stock}")
    print(f"Signal: {signal}")

if __name__ == "__main__":
    stock = input("Enter stock symbol (e.g. AAPL): ")
    run_bot(stock)
