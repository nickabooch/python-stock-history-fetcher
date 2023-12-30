# python-stock-history-fetcher
Python script using yfinance and pandas to download daily stock opening prices for a specified ticker and date range (e.g., 2023) and export to CSV. (Completed ~Dec 2023)



# Python Stock History Fetcher

## Overview
This project contains a Python script that utilizes the `yfinance` library to download historical stock data for a specified ticker symbol and date range. It specifically extracts the daily opening prices and saves them into a CSV file using the `pandas` library.

This script demonstrates:
* Interacting with financial data APIs (`yfinance`).
* Data handling and manipulation using `pandas` DataFrames.
* Exporting data to CSV format.

## Technology Stack
* Python 3
* Libraries:
    * `yfinance`
    * `pandas`

## Setup
1.  Ensure you have Python 3 installed.
2.  Clone or download this repository.
3.  Install the required libraries:
    ```bash
    pip install yfinance pandas
    ```

## Usage
1.  Modify the following variables within the `STOCKHISTORY.py` script as needed:
    * `ticker_symbol`: The stock ticker symbol you want to fetch data for (e.g., 'AAPL', 'GOOG').
    * `start_date`: The beginning of the date range (format: 'YYYY-MM-DD').
    * `end_date`: The end of the date range (format: 'YYYY-MM-DD').
2.  Navigate to the project directory in your terminal:
    ```bash
    cd path/to/python-stock-history-fetcher
    ```
3.  Run the script:
    ```bash
    python STOCKHISTORY.py
    ```
4.  A CSV file named `<ticker_symbol>_YYYY_opening_prices.csv` (e.g., `MPW_2023_opening_prices.csv`) will be created in the same directory containing the daily opening prices.

*(Disclaimer: Stock market data provided by yfinance may have limitations or inaccuracies. Use responsibly.)*
