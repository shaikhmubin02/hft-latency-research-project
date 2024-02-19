class MarketIntegrityEvaluator:
    def __init__(self, latency):
        self.latency = latency

    def evaluate_market_integrity(self):
        # Simulate evaluation of market integrity based on latency
        if self.latency < 1:
            return "Extremely low-latency practices may raise concerns about fair and orderly market functioning."
        else:
            return "Standard latency strategies contribute to market liquidity and efficiency but are subject to market impact risk."

def evaluate_market_integrity():
    latency_levels = [0.5, 2, 10]  # Different latency levels to evaluate

    for latency in latency_levels:
        evaluator = MarketIntegrityEvaluator(latency)
        integrity_status = evaluator.evaluate_market_integrity()
        print(f"For latency of {latency} milliseconds: {integrity_status}")

if __name__ == "__main__":
    evaluate_market_integrity()
