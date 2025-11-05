import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 2, 3, 4, 5])
y = np.array([10, 15, 25, 20, 30])
data = np.random.randn(1000)

plt.figure(figsize=(10, 8))

plt.subplot(2, 2, 1)
plt.bar(x, y, color='skyblue', edgecolor='black')
plt.title("Bar Chart")
plt.xlabel("X values")
plt.ylabel("Y values")

plt.subplot(2, 2, 2)
plt.hist(data, bins=20, color='lightgreen', edgecolor='black')
plt.title("Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")

plt.subplot(2, 2, 3)
plt.scatter(x, y, color='red')
plt.title("Scatter Plot")
plt.xlabel("X values")
plt.ylabel("Y values")


plt.subplot(2, 2, 4)
plt.plot(x, y, color='purple', marker='o', linestyle='-')
plt.title("Line Graph")
plt.xlabel("X values")
plt.ylabel("Y values")

plt.tight_layout()

plt.show()
