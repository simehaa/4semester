import numpy as np
import matplotlib.pyplot as plt

def x(t):
    return 1 - ((np.exp(2*t) - 1)/(np.exp(2*t) + 1))**2

t = np.linspace(-5,5,100)

plt.plot(t,x(t))
plt.legend(['dx/dt'])
plt.show()
