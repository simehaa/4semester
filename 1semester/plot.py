import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.where(x < 0, 0.0, 1.0)

n = 10000
x = np.linspace(-10, 10, n+1)

plt.plot(x, f(x))
plt.xlabel("x")
plt.ylabel("y")
plt.yaxis(-0.1, 1.1)
plt.title("plot")
plt.legend(["heaviside"])
plt.show()
