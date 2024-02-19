import random

class LowLatencyStrategy:
    def __init__(self, latency):
        self.latency = latency

    def execute_order(self, current_price):
        # Simulating order execution with latency
        execution_time = self.latency + random.randint(1, 10)  # Adding random delay
        
        # Simulating slippage based on latency
        if execution_time <= 5:
            # Orders executed within 5 milliseconds experience minimal slippage
            slippage = 0.01 * random.uniform(-1, 1)  # Simulating small slippage
        else:
            # Orders not executed within 5 milliseconds experience moderate slippage
            slippage = 0.05 * random.uniform(-1, 1)  # Simulating moderate slippage
        # Calculate executed price with slippage
        executed_price = current_price + slippage
        return executed_price

def simulate_market_impact(strategy, initial_price, num_trades):
    current_price = initial_price
    total_order_flow = 0
    for _ in range(num_trades):
        executed_price = strategy.execute_order(current_price)
        total_order_flow += 1
        current_price = executed_price
    return total_order_flow

def analyze_market_impact():
    extreme_low_latency_strategy = LowLatencyStrategy(latency=0.5)  # Extreme low latency setup
    standard_low_latency_strategy = LowLatencyStrategy(latency=2)  # Standard low latency setup

    initial_price = 100  # Initial market price
    num_trades = 1000  # Number of trades to simulate

    extreme_low_latency_order_flow = simulate_market_impact(extreme_low_latency_strategy, initial_price, num_trades)
    standard_low_latency_order_flow = simulate_market_impact(standard_low_latency_strategy, initial_price, num_trades)

    print("Market Impact Analysis:")
    print(f"Extreme Low Latency Order Flow: {extreme_low_latency_order_flow}")
    print(f"Standard Low Latency Order Flow: {standard_low_latency_order_flow}")

if __name__ == "__main__":
    analyze_market_impact()
