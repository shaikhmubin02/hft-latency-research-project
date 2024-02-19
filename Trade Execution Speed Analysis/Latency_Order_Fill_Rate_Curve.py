import numpy as np
import matplotlib.pyplot as plt

# Example latency values (in milliseconds)
latency = [10, 20, 30, 40, 50]

# Example order fill rates (in percentage)
fill_rate = [85, 80, 75, 70, 65]  # fill rates corresponding to latency values

# Plot the curve
plt.figure(figsize=(8, 6))
plt.plot(latency, fill_rate, marker='o', linestyle='-')
plt.title('Relationship between Latency and Order Fill Rate')
plt.xlabel('Latency (ms)')
plt.ylabel('Order Fill Rate (%)')
plt.grid(True)
plt.show()
