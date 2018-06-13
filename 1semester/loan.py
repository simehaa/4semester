import numpy as np
import matplotlib.pyplot as plt

N = 100 # months
p = 3.6 # % rent

x = np.zeros(N)
y = np.zeros(N)
x[0] = 1000
y[0] = 5000

for i in range(N-1):
    y[i + 1] = (p/(12*100))*x[i] + (x[0]/N)
    x[i + 1] = x[i] + (p/(12*100))*x[i] - y[i + 1]

plt.plot(x,y)
plt.show()
