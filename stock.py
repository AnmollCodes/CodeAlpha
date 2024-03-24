from alpha_vantage.timeseries import TimeSeries
import json

portfolio = {}

def add_stock(ticker, shares, price):
    "|| New Stock ||"
    try:
        ts = TimeSeries(key='CKYGD18W6GKTI14F', output_format='json')
        data, meta_data = ts.get_quote_endpoint(symbol=ticker)
        if '05. price' in data:
            if ticker not in portfolio:
                portfolio[ticker] = {
                    'shares': 0,
                    'cost': 0,
                    'price': 0
                }
            portfolio[ticker]['shares'] += shares
            portfolio[ticker]['cost'] += shares * price
            portfolio[ticker]['price'] = float(data['05. price'])
        else:
            print(f"Sorry! Can't get price for {ticker}.")
    except Exception as e:
        print(f"Error: {e}")

def remove_stock(ticker, shares):
    """Remove a stock from the portfolio."""
    if ticker not in portfolio:
        return
    portfolio[ticker]['shares'] -= shares
    portfolio[ticker]['cost'] -= shares * portfolio[ticker]['price']
    if portfolio[ticker]['shares'] <= 0:
        del portfolio[ticker]

def get_portfolio():
    """Return the current portfolio."""
    return portfolio

# Example usage
add_stock('AAPL', 10, 150)
add_stock('GOOG', 20, 1000)
print(json.dumps(get_portfolio()))
remove_stock('AAPL', 5)
print(json.dumps(get_portfolio()))
