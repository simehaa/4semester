import numpy as np
from math import sqrt
import matplotlib.pyplot as plt

k = np.linspace(-5,5,1001)
x = np.linspace(-10,10,1001)
a = 1
A = a/(k**2 + a**2)
y = A*np.sin(x*k)

plt.plot(x,y)
plt.show()
