import random

class HFTStrategy:
    def __init__(self, latency):
        self.latency = latency

    def execute_order(self, order_type):
        
        # Here, latency is simulated by adding a random delay
        execution_time = self.latency + random.randint(1, 10)  
        # Simulating order fill based on latency
        fill_rate = 0
        if execution_time <= 5:  # Orders executed within 5 milliseconds are considered filled
            fill_rate = 1
        elif execution_time <= 10:  # Orders executed within 10 milliseconds are partially filled
            fill_rate = 0.5
        else:
            fill_rate = 0  # Orders not executed within 10 milliseconds are not filled
        return fill_rate

def compare_fill_rates():
    low_latency_strategy = HFTStrategy(latency=1)  # Low latency setup
    moderate_latency_strategy = HFTStrategy(latency=5)  # Moderate latency setup

    num_orders = 1000
    low_latency_fill_count = 0
    moderate_latency_fill_count = 0

    for _ in range(num_orders):
        low_latency_fill_count += low_latency_strategy.execute_order("buy")
        moderate_latency_fill_count += moderate_latency_strategy.execute_order("buy")

    low_latency_fill_rate = low_latency_fill_count / num_orders
    moderate_latency_fill_rate = moderate_latency_fill_count / num_orders

    print("Fill Rates:")
    print(f"Low Latency: {low_latency_fill_rate * 100:.2f}%")
    print(f"Moderate Latency: {moderate_latency_fill_rate * 100:.2f}%")

if __name__ == "__main__":
    compare_fill_rates()
