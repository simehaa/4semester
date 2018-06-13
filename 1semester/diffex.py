import numpy as np
import matplotlib.pyplot as plt
from math import *

def f(t, x):
    return x

n = int(raw_input('Values: '))
s0 = float(raw_input('Start: '))
s1 = float(raw_input('Stop: '))
h = (s1 - s0)/float(n)

x = np.zeros(n + 1)
t = np.zeros(n + 1)

x[0] = s0
t[0] = exp(s0)

for i in range(n):
    x[i + 1] = x[0] + h*(i + 1)
    t[i + 1] = t[i] + h*f(x[i],t[i])

plt.plot(x,t, label='Eulers')
plt.grid(True)
plt.show()
