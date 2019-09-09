import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Generate random values
# x = np.random.random_integers(1000, 1700, 100)
# y = np.random.random_integers(1000, 1700, 100)
dataset = pd.read_csv("linear_dataset.csv", sep=',', header=None).to_numpy()
x = dataset[..., 0:1]
y = dataset[..., 1:2]

# Calculate mean for x & y
mean_x = np.mean(x)
mean_y = np.mean(y)

# Required declaration
total_values = len(x)
var1 = 0
var2 = 0

# Implement simple linear equation formula
for i in range(total_values):
    var1 += (x[i] - mean_x) * (y[i] - mean_y)
    var2 += (x[i] - mean_x) ** 2

# Known formula to calculate slope and const
slope = var1 / var2
const = mean_y - (slope * mean_x)
print(slope, const)

# To plot the graph
max_value = np.max(x)
min_value = np.min(x)

# Here, pass a few points to draw the straight line
a = np.linspace(min_value, max_value, 1000)
b = const + slope * a

# Plot points and line
plt.plot(a, b, color="#58b970", label="Regression line")
plt.scatter(x, y, c='#ef5423', label="Scatter points")
plt.xlabel("Independent")
plt.ylabel("Dependent")
plt.legend()
plt.show()
