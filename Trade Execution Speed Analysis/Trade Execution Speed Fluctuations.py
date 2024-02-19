import matplotlib.pyplot as plt
import numpy as np

# Example data
timestamps = np.arange(0, 100, 1)  # timestamps
latency = np.random.normal(50, 10, size=len(timestamps))  # latency
execution_speed = np.random.normal(100, 20, size=len(timestamps))  # execution speed fluctuations (random)

# Plot the overlaid time series chart 
fig, ax1 = plt.subplots(figsize=(10, 6))

color = 'tab:blue'
ax1.set_xlabel('Time')
ax1.set_ylabel('Latency (ms)', color=color)
ax1.plot(timestamps, latency, color=color, label='Latency')
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx() 
color = 'tab:red'
ax2.set_ylabel('Execution Speed', color=color)
ax2.plot(timestamps, execution_speed, color=color, label='Execution Speed', linestyle='--')
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout(rect=[0, 0.03, 1, 0.95]) 
plt.title('Latency and Trade Execution Speed Over Time', pad=20) 
plt.show()
