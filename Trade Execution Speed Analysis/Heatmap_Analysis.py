import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Example latency levels (in milliseconds)
latency_levels = [10, 20, 30, 40, 50]

# Example order sizes
order_sizes = [100, 200, 300, 400, 500]

# Example fill rates matrix 
fill_rates = np.array([
    [0.85, 0.78, 0.72, 0.65, 0.60],
    [0.80, 0.74, 0.68, 0.62, 0.58],
    [0.75, 0.70, 0.65, 0.60, 0.55],
    [0.70, 0.65, 0.60, 0.55, 0.50],
    [0.65, 0.60, 0.55, 0.50, 0.45]
])

# Plot heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(fill_rates, annot=True, fmt=".2f", cmap="YlGnBu", xticklabels=order_sizes, yticklabels=latency_levels)
plt.title('Order Fill Rates Across Latency and Order Size')
plt.xlabel('Order Size')
plt.ylabel('Latency (ms)')
plt.show()
