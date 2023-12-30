import yfinance as yf
import pandas as pd

# Define the ticker symbol for Uhaul. Replace 'UHAL' with the correct symbol if different.
ticker_symbol = 'MPW'

# Define the start and end dates for the year 2023.
start_date = '2023-01-01'
end_date = '2023-12-31'

# Fetch the historical data for the ticker.
data = yf.download(ticker_symbol, start=start_date, end=end_date)

# Filter out only the 'Open' prices.
opening_prices = data['Open']

# Save the data to a CSV file or process as needed.
opening_prices.to_csv(f'{ticker_symbol}_2023_opening_prices.csv')

print(opening_prices.head())  # Print the first few rows as a check.
