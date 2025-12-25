import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt


# To fetch the stock data
def fetch_stock_data(ticker, period="1y"):
    # We need past data to extract volatility (std dev) and mean return
    stock_data = yf.download(ticker, period=period)
    return stock_data


# To calculate the daily returns and standard deviation of the returns
def calculate_returns_and_std(prices):
    daily_return = np.diff(prices) / prices[:-1]
    
    # Calculate volatility (standard deviation of returns)
    daily_std = np.std(daily_return)
    return daily_return, daily_std


# Plotting the graphs for the past data
def plot_data(dates, prices, daily_returns):
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 12))

    # Plot 1: Historical or Forecasted Price Path
    ax1.plot(dates, prices, label='Price')
    ax1.set_title("Stock/Simulated Price")
    ax1.set_ylabel("Prices")
    ax1.legend()

    # Plot 2: Daily Returns Over Time
    ax2.plot(dates[1:], daily_returns, label='Daily Returns', color='orange')
    ax2.set_title("Daily Returns")
    ax2.set_ylabel("Returns")
    ax2.legend()

    # Plot 3: Histogram (Distribution) of Returns
    ax3.hist(daily_returns, bins=50, color='purple', alpha=0.7)
    ax3.set_title("Distribution of Returns")
    ax3.set_ylabel("Frequency")
    ax3.set_xlabel("Daily Returns")

    plt.tight_layout()
    plt.show()


def generate_random_walk(start_price, num_of_steps, mu=0, sigma=1):
    # Generate random returns from normal distribution
    # mu (mean) = average daily return (slight drift up/down)
    # sigma (std dev) = volatility - tells us the "wiggle" magnitude
    random_returns = np.random.normal(mu, sigma, num_of_steps)

    # Initialize empty array to store simulated prices
    prices = np.empty(num_of_steps)
    prices[0] = start_price

    # Build price path step-by-step
    # This is the essence of random walk: past doesn't predict future, only randomness matters
    for timestep in range(1, num_of_steps):
        prices[timestep] = prices[timestep - 1] * (1 + random_returns[timestep - 1])
    
    return prices


# ==== MAIN EXECUTION ====

# Step 1: Compiling Historical Data
# We analyze JPM to understand its historical volatility and return distribution
ticker = "JPM"                  #Imp: You can change the ticker to any other stock you would like to research on!
stock_data = fetch_stock_data(ticker)

# Step 2: Extracting Historical Statistics
historical_prices = stock_data['Close'].values
historical_returns, historical_std = calculate_returns_and_std(historical_prices)
print(f"The historical returns for {ticker}: {historical_std}")

# Step 3: Visualising Historical Data
# Three charts show: price trend, volatility pattern, and return distribution
dates = stock_data.index
plot_data(dates, historical_prices, historical_returns)

# ==== RANDOM WALK FORECASTING ====

# Step 4: Forecasting Parameters
start_price = stock_data['Close'].values[-1]
num_of_steps = 272
mu = np.mean(historical_returns)
sigma = np.std(historical_returns)

# Step 5: Generating Random Walk Fprecast
forecasted_prices = generate_random_walk(start_price, num_of_steps, mu=mu, sigma=sigma)
forecasted_returns, forecasted_std = calculate_returns_and_std(forecasted_prices)

# Step 6: Visualising
plot_data([*range(272)], forecasted_prices, forecasted_returns)
