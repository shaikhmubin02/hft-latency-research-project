import random

class HFTStrategy:
    def __init__(self, latency):
        self.latency = latency

    def execute_order(self, order_type, current_price):

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

def compare_slippage():
    low_latency_strategy = HFTStrategy(latency=1)  # Low latency setup
    moderate_latency_strategy = HFTStrategy(latency=5)  # Moderate latency setup

    current_price = 100  # Current market price

    num_orders = 1000
    low_latency_slippage_total = 0
    moderate_latency_slippage_total = 0

    for _ in range(num_orders):
        low_latency_slippage_total += abs(low_latency_strategy.execute_order("buy", current_price) - current_price)
        moderate_latency_slippage_total += abs(moderate_latency_strategy.execute_order("buy", current_price) - current_price)

    low_latency_average_slippage = low_latency_slippage_total / num_orders
    moderate_latency_average_slippage = moderate_latency_slippage_total / num_orders

    print("Slippage Analysis:")
    print(f"Low Latency Average Slippage: {low_latency_average_slippage:.2f}")
    print(f"Moderate Latency Average Slippage: {moderate_latency_average_slippage:.2f}")

if __name__ == "__main__":
    compare_slippage()
