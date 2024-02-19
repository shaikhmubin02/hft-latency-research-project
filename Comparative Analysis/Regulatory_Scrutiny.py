class ComplianceChecker:
    def __init__(self, latency):
        self.latency = latency

    def check_regulatory_compliance(self):
        
        # Simulate regulatory compliance checks based on latency
        if self.latency < 1:
            return "Low-latency strategies may attract regulatory scrutiny due to potential market abuse."
        else:
            return "Standard latency strategies are subject to regulatory oversight, but extreme low-latency practices may face increased scrutiny."

def explore_regulatory_compliance():
    latency_levels = [0.5, 2, 10]  # Different latency levels to explore

    for latency in latency_levels:
        checker = ComplianceChecker(latency)
        regulatory_status = checker.check_regulatory_compliance()
        print(f"For latency of {latency} milliseconds: {regulatory_status}")

if __name__ == "__main__":
    explore_regulatory_compliance()
