import pandas as pd
import matplotlib.pyplot as plt

# Example Data 
data = {
    "Latency": [5, 12, 20, 8, 15, 25, 32, 40, 18, 10, 38, 22, 45, 11, 30],
    "Trade Execution Speed": [120, 85, 100, 78, 92, 115, 130, 142, 88, 75, 128, 95, 150, 82, 118]
}

# DataFrame for organization
df = pd.DataFrame(data)

# latency bins
bins = [0, 10, 20, 30, 40, 50]

# Latency Bin
df['Latency Bin'] = pd.cut(df['Latency'], bins=bins)

# Calculate average trade execution speed per bin
df_grouped = df.groupby('Latency Bin')['Trade Execution Speed'].mean()

# Bar Chart Visualization
df_grouped.plot(kind='bar')
plt.title("Average Trade Execution Speed by Latency Bin")
plt.xlabel("Latency Bin (ms)")
plt.ylabel("Average Trade Execution Speed (ms)")
plt.show()

# Optional: Line Graph Visualization
df_grouped.plot()  # Uses default line plot
plt.title("Average Trade Execution Speed by Latency Bin")
plt.xlabel("Latency Bin (ms)")
plt.ylabel("Average Trade Execution Speed (ms)")
plt.show()
