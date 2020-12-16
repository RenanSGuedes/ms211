import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, num=100)

fx = []

for i in range(len(x)):
  a = x[i]**2 - 2*x[i] + 5
  fx.append(a)

print(a == float(x[i]**2 - 2*x[i] + 5))
plt.plot(x, fx)

plt.show()