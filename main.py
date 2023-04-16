import numpy as np
import matplotlib.pyplot as plt

x = [2, 6, 4, 3, 3]
y = [1, 5, 2, 5, 7]

x = np.array(x)
y = np.array(y)

m, b = np.polyfit(x, y, 1)

prediction = m * x + b

plt.scatter(x, y)
plt.plot(x, prediction, color='blue')
plt.show()