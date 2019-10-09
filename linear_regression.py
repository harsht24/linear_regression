import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

dataset = pd.read_csv("content/linear_dataset.csv", header=None).to_numpy()
# print(dataset.shape)
# print(dataset.head())

x = dataset[..., 0:1]
# print(x)
y = dataset[..., 1:2]
# print(y)

mean_x = np.mean(x)
mean_y = np.mean(y)
# print(mean_x, mean_y)

total_values = len(x)

num, den = 0, 0
for i in range(total_values):
    num += (x[i] - mean_x) * (y[i] - mean_y)
    den += (x[i] - mean_x) ** 2

slope = num / den
const = mean_y - slope * mean_x

print("Slope = {}".format(slope), "Intercept = {}".format(const))

a = np.linspace(np.min(x), np.max(x), 1000)
b = const + slope * a

plt.plot(a, b, color='RED', label='Regression line')
plt.scatter(x, y, color='BLUE', label='Scatter plot')
plt.xlabel('Study Hours')
plt.ylabel('Marks')
plt.legend()
plt.show()

# Predicted values
y_pred = const + slope * x

# Root-mean-squared-error
rmse = 0
for i in range(total_values):
    rmse += (y_pred[i] - y[i]) ** 2

rmse = np.sqrt(rmse / total_values)
print("Root mean squared error : {}".format(rmse))

# Evaluating R2 Score
ss_t, ss_r = 0, 0
for i in range(total_values):
    ss_t += (y[i] - mean_y) ** 2
    ss_r += (y[i] - y_pred[i]) ** 2

r2_score = 1 - (ss_r / ss_t)
print("R2 Score : {}".format(r2_score))
