import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset=pd.read_csv('Salary_Data.csv')

x=dataset['YearsExperience']
y=dataset['Salary']

mean_x = np.mean(x)
mean_y = np.mean(y)
length_of_x = np.size(x)

b = np.sum(x * y) - mean_x * mean_y * length_of_x
b1 = np.sum(x * x) - length_of_x*mean_x ** 2

a1 = b / b1
a0 = mean_y - a1 * mean_x

print(a1)
print(a0)

max_value = np.max(x)
min_value = np.min(x)
a = np.linspace(min_value, max_value, 1000)
final_line = a0 + a1 * a

plt.plot(a,final_line)
plt.plot(a, final_line, label="Line")
plt.scatter(x, y, label="Points")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.legend()
plt.show()
