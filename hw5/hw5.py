import yfinance as yf
import pandas as pd
import json

# Required stocks + 7 additional Nasdaq stocks
stocks = [
    "AAPL", "GOOG", "ADBE",
    "MSFT", "AMZN", "META",
    "NVDA", "CSCO", "INTC", "NFLX"
]

results = {}

# ----------------------------------
# Mean Reversion Strategy
# Buy when price is below MA
# Sell when price is above MA
# ----------------------------------
def mean_reversion_strategy(data):
    data["MA20"] = data["Close"].rolling(20).mean()

    cash = 10000
    shares = 0

    for i in range(20, len(data)):
        price = data["Close"].iloc[i]
        ma = data["MA20"].iloc[i]

        if price < ma and shares == 0:
            shares = cash / price
            cash = 0

        elif price > ma and shares > 0:
            cash = shares * price
            shares = 0

    if shares > 0:
        cash = shares * data["Close"].iloc[-1]

    return round(cash, 2)


# ----------------------------------
# SMA Strategy
# Buy when price crosses above MA
# Sell when price crosses below MA
# ----------------------------------
def sma_strategy(data):
    data["MA20"] = data["Close"].rolling(20).mean()

    cash = 10000
    shares = 0

    for i in range(21, len(data)):
        prev_price = data["Close"].iloc[i - 1]
        prev_ma = data["MA20"].iloc[i - 1]

        curr_price = data["Close"].iloc[i]
        curr_ma = data["MA20"].iloc[i]

        # Cross above MA -> Buy
        if prev_price <= prev_ma and curr_price > curr_ma and shares == 0:
            shares = cash / curr_price
            cash = 0

        # Cross below MA -> Sell
        elif prev_price >= prev_ma and curr_price < curr_ma and shares > 0:
            cash = shares * curr_price
            shares = 0

    if shares > 0:
        cash = shares * data["Close"].iloc[-1]

    return round(cash, 2)


# Run simulations
for ticker in stocks:
    data = yf.download(ticker, period="1y", auto_adjust=True)

    mean_result = mean_reversion_strategy(data.copy())
    sma_result = sma_strategy(data.copy())

    results[ticker] = {
        "Mean Reversion": mean_result,
        "Simple Moving Average": sma_result
    }

# Save results to JSON
with open("results.json", "w") as outfile:
    json.dump(results, outfile, indent=4)

print("Results saved to results.json")

import json

# --------------------------------------------------
# Mean Reversion Strategy
# Buy when price is below MA
# Sell when price is above MA
# --------------------------------------------------
def meanReversionStrategy(prices):

    moving_average_days = 4
    money = 1000.0
    shares = 0.0
    starting_money = money

    for i in range(moving_average_days, len(prices)):

        moving_average = sum(prices[i-moving_average_days:i]) / moving_average_days
        current_price = prices[i]

        # Buy
        if current_price < moving_average and shares == 0:
            shares = money / current_price
            money = 0
            print("BUY at $", round(current_price, 2))

        # Sell
        elif current_price > moving_average and shares > 0:
            money = shares * current_price
            shares = 0
            print("SELL at $", round(current_price, 2))

    # Sell remaining shares at end
    if shares > 0:
        money = shares * prices[-1]

    profit = money - starting_money
    returns_percent = (profit / starting_money) * 100

    return profit, returns_percent


# --------------------------------------------------
# Simple Moving Average Strategy
# Buy when price crosses ABOVE MA
# Sell when price crosses BELOW MA
# --------------------------------------------------
def simpleMovingAverageStrategy(prices):

    moving_average_days = 4
    money = 1000.0
    shares = 0.0
    starting_money = money

    for i in range(moving_average_days + 1, len(prices)):

        previous_price = prices[i - 1]
        current_price = prices[i]

        previous_ma = sum(
            prices[i - moving_average_days - 1:i - 1]
        ) / moving_average_days

        current_ma = sum(
            prices[i - moving_average_days:i]
        ) / moving_average_days

        # Cross above MA -> Buy
        if (previous_price <= previous_ma and
                current_price > current_ma and
                shares == 0):

            shares = money / current_price
            money = 0
            print("BUY at $", round(current_price, 2))

        # Cross below MA -> Sell
        elif (previous_price >= previous_ma and
              current_price < current_ma and
              shares > 0):

            money = shares * current_price
            shares = 0
            print("SELL at $", round(current_price, 2))

    # Sell remaining shares at end
    if shares > 0:
        money = shares * prices[-1]

    profit = money - starting_money
    returns_percent = (profit / starting_money) * 100

    return profit, returns_percent


# --------------------------------------------------
# Save Results
# --------------------------------------------------
def saveResults(results):

    with open("results.json", "w") as outfile:
        json.dump(results, outfile, indent=4)

    print("Results saved to results.json")