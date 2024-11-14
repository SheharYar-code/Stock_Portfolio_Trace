import yfinance as yf

class StockPortfolio:
    def __init__(self):
        self.portfolio = {}

    def add_stock(self, ticker, quantity):
        """
        Adds a stock to the portfolio.
        :param ticker: The stock ticker symbol (e.g., 'AAPL' for Apple).
        :param quantity: The number of shares purchased.
        """
        if ticker in self.portfolio:
            self.portfolio[ticker]['quantity'] += quantity
        else:
            stock_info = yf.Ticker(ticker).info
            self.portfolio[ticker] = {
                'quantity': quantity,
                'price': stock_info['currentPrice'],
                'name': stock_info['longName']
            }
        print(f"Added {quantity} shares of {ticker} to the portfolio.")

    def remove_stock(self, ticker, quantity):
        """
        Removes a stock from the portfolio.
        :param ticker: The stock ticker symbol.
        :param quantity: The number of shares to remove.
        """
        if ticker in self.portfolio:
            if self.portfolio[ticker]['quantity'] > quantity:
                self.portfolio[ticker]['quantity'] -= quantity
                print(f"Removed {quantity} shares of {ticker} from the portfolio.")
            elif self.portfolio[ticker]['quantity'] == quantity:
                del self.portfolio[ticker]
                print(f"Removed {ticker} from the portfolio.")
            else:
                print("Quantity exceeds the holdings in the portfolio.")
        else:
            print("Stock not found in the portfolio.")

    def get_portfolio(self):
        """
        Returns the current state of the portfolio.
        """
        for ticker, data in self.portfolio.items():
            current_price = yf.Ticker(ticker).info['currentPrice']
            total_investment = data['price'] * data['quantity']
            current_value = current_price * data['quantity']
            gain_loss = current_value - total_investment
            print(f"{data['name']} ({ticker}):")
            print(f"  Shares: {data['quantity']}")
            print(f"  Purchase Price: ${data['price']:.2f}")
            print(f"  Current Price: ${current_price:.2f}")
            print(f"  Total Investment: ${total_investment:.2f}")
            print(f"  Current Value: ${current_value:.2f}")
            print(f"  Gain/Loss: ${gain_loss:.2f}")
            print("")

# Example usage:
portfolio = StockPortfolio()
portfolio.add_stock('AAPL', 10)  # Add 10 shares of Apple
portfolio.add_stock('GOOGL', 5)  # Add 5 shares of Google
portfolio.get_portfolio()        # View portfolio and performance
portfolio.remove_stock('AAPL', 5)  # Remove 5 shares of Apple
portfolio.get_portfolio()        # View updated portfolio
