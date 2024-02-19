import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Example data 
latency = np.array([20, 25, 30, 35, 40]).reshape(-1, 1)  # latency
execution_speed = np.array([100, 95, 90, 85, 80])  # trade execution speed measurements

# Fit linear regression model
regression_model = LinearRegression()
regression_model.fit(latency, execution_speed)

# Predict trade execution speed using regression model
predicted_speed = regression_model.predict(latency)

# Visualize regression line on scatter plot
plt.figure(figsize=(8, 6))
plt.scatter(latency, execution_speed, color='blue', label='Actual Data')
plt.plot(latency, predicted_speed, color='red', label='Regression Line')
plt.title('Regression Analysis: Latency vs. Trade Execution Speed')
plt.xlabel('Latency')
plt.ylabel('Trade Execution Speed')
plt.legend()
plt.grid(True)
plt.show()
