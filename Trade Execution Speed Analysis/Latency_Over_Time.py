import matplotlib.pyplot as plt
import numpy as np

# Example data
timestamps = np.arange(0, 100, 1)  # timestamps
latency = np.random.normal(50, 10, size=len(timestamps))  # latency

# Plot the time series chart
plt.figure(figsize=(10, 6))
plt.plot(timestamps, latency, marker='o', linestyle='-')
plt.title('Latency Over Time')
plt.xlabel('Time')
plt.ylabel('Latency (ms)')
plt.grid(True)
plt.show()
