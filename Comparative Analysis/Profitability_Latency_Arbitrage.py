import random

class LatencyArbitrageStrategy:
    def __init__(self, latency_difference):
        self.latency_difference = latency_difference

    def execute_arbitrage(self, price_feed_1, price_feed_2):
        # Simulate latency arbitrage by comparing prices from two feeds
        if price_feed_1 < price_feed_2:
            profit = price_feed_2 - price_feed_1
        else:
            profit = 0  # No profit opportunity if price_feed_1 >= price_feed_2
        return profit

def simulate_latency_arbitrage(latency_difference, num_trades):
    total_profit = 0
    for _ in range(num_trades):
        # Simulating prices from two different feeds
        price_feed_1 = random.uniform(90, 110)
        price_feed_2 = random.uniform(90, 110)
        # Introducing latency difference between feeds
        price_feed_2 += latency_difference
        # Executing latency arbitrage
        strategy = LatencyArbitrageStrategy(latency_difference)
        profit = strategy.execute_arbitrage(price_feed_1, price_feed_2)
        total_profit += profit
    return total_profit

def analyze_latency_arbitrage():
    num_trades = 1000  # Number of trades to simulate
    latency_differences = [0.1, 0.01, 0.001]  # Latency differences to test

    for latency_difference in latency_differences:
        total_profit = simulate_latency_arbitrage(latency_difference, num_trades)
        print(f"Profitability with Latency Difference of {latency_difference} seconds: ${total_profit:.2f}")

if __name__ == "__main__":
    analyze_latency_arbitrage()
