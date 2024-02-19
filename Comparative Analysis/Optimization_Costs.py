import random
import time

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

class ExtremeLowLatencyStrategy:
    def execute_order(self, current_price):
        # Simulating order execution with extreme low latency
        # No delay introduced for extreme low-latency strategy
        # Simulating slippage (can be adjusted based on specific behavior)
        slippage = 0.005 * random.uniform(-1, 1)  # Simulating minimal slippage
        executed_price = current_price + slippage
        return executed_price

def simulate_optimization_costs(strategy, initial_price, num_trades):
    total_execution_time = 0
    for _ in range(num_trades):
        start_time = time.time()
        strategy.execute_order(initial_price)
        end_time = time.time()
        total_execution_time += (end_time - start_time)
    return total_execution_time

def compare_optimization_costs():
    initial_price = 100  # Initial market price
    num_trades = 1000  # Number of trades to simulate

    standard_low_latency_strategy = LowLatencyStrategy(latency=2)  # Standard low latency setup
    extreme_low_latency_strategy = ExtremeLowLatencyStrategy()  # Extreme low latency setup

    standard_latency_execution_time = simulate_optimization_costs(standard_low_latency_strategy, initial_price, num_trades)
    extreme_latency_execution_time = simulate_optimization_costs(extreme_low_latency_strategy, initial_price, num_trades)

    print("Optimization Costs Comparison:")
    print(f"Standard Low Latency Strategy Execution Time: {standard_latency_execution_time:.6f} seconds")
    print(f"Extreme Low Latency Strategy Execution Time: {extreme_latency_execution_time:.6f} seconds")

if __name__ == "__main__":
    compare_optimization_costs()
