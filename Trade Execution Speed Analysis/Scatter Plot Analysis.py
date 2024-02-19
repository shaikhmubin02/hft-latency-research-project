import matplotlib.pyplot as plt
import seaborn as sns

# Example data
data = {
    "Latency": [5, 12, 20, 8, 15, 25, 32, 40, 18, 10, 38, 22, 45, 11, 30],
    "Trade Execution Speed": [120, 85, 100, 78, 92, 115, 130, 142, 88, 75, 128, 95, 150, 82, 118]
}

# Scatter Plot Analysis
sns.scatterplot(x="Latency", y="Trade Execution Speed", data=data)
plt.title("Trade Execution Speed vs. Latency")
plt.xlabel("Latency (ms)")
plt.ylabel("Trade Execution Speed (ms)")
plt.show()
