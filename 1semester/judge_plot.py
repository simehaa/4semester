import numpy as np
from numpy import cos, pi
x = np.linspace(0,2,1000)
y = cos(18*pi*x)
import matplotlib.pyplot as plt
plt.plot(x, y)
plt.show()
