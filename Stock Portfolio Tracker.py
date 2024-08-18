import requests
import pandas as pd

# Replace 'YOUR_API_KEY' with your actual Alpha Vantage API key
API_KEY = 'YOUR_API_KEY'
BASE_URL = 'https://www.alphavantage.co/query'

portfolio = {}

def get_stock_price(symbol):
    params = {
        'function': 'TIME_SERIES_INTRADAY',
        'symbol': symbol,
        'interval': '1min',
        'apikey': API_KEY
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    if 'Time Series (1min)' in data:
        latest_time = list(data['Time Series (1min)'].keys())[0]
        return float(data['Time Series (1min)'][latest_time]['1. open'])
    else:
        print(f"Error fetching data for {symbol}")
        return None

def add_stock(symbol, shares):
    price = get_stock_price(symbol)
    if price:
        portfolio[symbol] = {'shares': shares, 'price': price}
        print(f"Added {shares} shares of {symbol} at ${price:.2f} each.")

def remove_stock(symbol):
    if symbol in portfolio:
        del portfolio[symbol]
        print(f"Removed {symbol} from portfolio.")
    else:
        print(f"{symbol} not found in portfolio.")

def view_portfolio():
    if portfolio:
        df = pd.DataFrame(portfolio).T
        df['total_value'] = df['shares'] * df['price']
        print(df)
        print(f"Total Portfolio Value: ${df['total_value'].sum():.2f}")
    else:
        print("Portfolio is empty.")

def main():
    while True:
        print("\nStock Portfolio Tracker")
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. View Portfolio")
        print("4. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            symbol = input("Enter stock symbol: ").upper()
            shares = int(input("Enter number of shares: "))
            add_stock(symbol, shares)
        elif choice == '2':
            symbol = input("Enter stock symbol to remove: ").upper()
            remove_stock(symbol)
        elif choice == '3':
            view_portfolio()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
