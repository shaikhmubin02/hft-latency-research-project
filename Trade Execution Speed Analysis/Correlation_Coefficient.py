import numpy as np

# Example data 
latency = np.array([20, 25, 30, 35, 40])  # latency measurements
execution_speed = np.array([100, 95, 90, 85, 80])  # trade execution speed measurements

# Calculate correlation coefficient
correlation_coefficient = np.corrcoef(latency, execution_speed)[0, 1]

print("Correlation coefficient between latency and trade execution speed:", correlation_coefficient)


