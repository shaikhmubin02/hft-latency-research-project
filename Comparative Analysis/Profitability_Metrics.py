import random

class HFTStrategy:
    def __init__(self, latency):
        self.latency = latency

    def execute_order(self, order_type, current_price):
        # Simulating order execution with latency
        execution_time = self.latency + random.randint(1, 10)  # Adding random delay
        # Simulating slippage based on latency
        if execution_time <= 5:
            # Orders executed within 5 milliseconds experience minimal slippage
            slippage = 0.01 * random.uniform(-1, 1)  # Simulating small slippage
        elif execution_time <= 10:
            # Orders executed within 10 milliseconds experience moderate slippage
            slippage = 0.05 * random.uniform(-1, 1)  # Simulating moderate slippage
        else:
            # Orders not executed within 10 milliseconds experience significant slippage
            slippage = 0.1 * random.uniform(-1, 1)  # Simulating significant slippage
        # Calculate executed price with slippage
        executed_price = current_price + slippage
        return executed_price

def simulate_trades(strategy, initial_price, num_trades):
    current_price = initial_price
    total_profit = 0
    for _ in range(num_trades):
        executed_price = strategy.execute_order("buy", current_price)
        profit = executed_price - current_price
        total_profit += profit
        current_price = executed_price
    return total_profit

def compare_profitability():
    low_latency_strategy = HFTStrategy(latency=1)  # Low latency setup
    moderate_latency_strategy = HFTStrategy(latency=5)  # Moderate latency setup

    initial_price = 100  # Initial market price
    num_trades = 1000  # Number of trades to simulate

    low_latency_profit = simulate_trades(low_latency_strategy, initial_price, num_trades)
    moderate_latency_profit = simulate_trades(moderate_latency_strategy, initial_price, num_trades)

    print("Profitability Metrics:")
    print(f"Low Latency Total Profit: ${low_latency_profit:.2f}")
    print(f"Moderate Latency Total Profit: ${moderate_latency_profit:.2f}")

if __name__ == "__main__":
    compare_profitability()
