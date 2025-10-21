# TASK 2: Stock Portfolio Tracker

# 1. Hardcode stock names and quantity
# A dictionary where keys are stock symbols and values are the number of shares owned.
my_portfolio = {
    'AAPL': 10,   # 10 shares of Apple
    'MSFT': 5,    # 5 shares of Microsoft
    'TSLA': 2     # 2 shares of Tesla
}

# 2. Use a hardcoded dictionary to define stock prices
# A dictionary where keys are stock symbols and values are their current price.
stock_prices = {
    'AAPL': 180.00,
    'MSFT': 320.50,
    'TSLA': 250.75,
    'GOOG': 150.00 # Include extra stocks that might not be in the portfolio
}

# Initialize the total investment value
total_value = 0.0

# 3. Calculate the total investment value
print("--- Portfolio Value Calculation ---")
print(f"Stock Prices Used: {stock_prices}")
print(f"Portfolio Holdings: {my_portfolio}")
print("-" * 35)

# Iterate through the stocks in the portfolio
for stock, quantity in my_portfolio.items():
    if stock in stock_prices:
        # Retrieve the price from the stock_prices dictionary
        price = stock_prices[stock]
        # Calculate the value for this specific holding
        holding_value = quantity * price
        
        # Add the holding value to the total portfolio value
        total_value += holding_value
        
        print(f"Stock: {stock} | Shares: {quantity} | Price: ${price:.2f} | Value: ${holding_value:.2f}")
    else:
        print(f"Warning: Price for {stock} not found. Skipping calculation for this stock.")

print("-" * 35)

# 4. Display total investment value
print(f"✅ Total Investment Value: ${total_value:.2f}")

# --- Optional: Save the result to a .txt file (File Handling) ---

output_filename = "portfolio_value.txt"

try:
    with open(output_filename, 'w') as f:
        f.write("Stock Portfolio Total Investment Value\n")
        f.write("-" * 35 + "\n")
        f.write(f"Total Value: ${total_value:.2f}\n")
        f.write("-" * 35 + "\n")
        f.write("Holdings Detail:\n")
        for stock, quantity in my_portfolio.items():
             if stock in stock_prices:
                price = stock_prices[stock]
                holding_value = quantity * price
                f.write(f"{stock}: {quantity} shares @ ${price:.2f} = ${holding_value:.2f}\n")
    print(f"\nResult saved successfully to {output_filename}")
except IOError:
    print(f"\nError: Could not write to file {output_filename}.")