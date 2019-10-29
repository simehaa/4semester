from __future__ import division
import matplotlib.pyplot as plt
import numpy as np

m = 90
k = 1
g = 9.81

def f(u, t):
    return (g/m - k*u**2/m)

n = 1000
T = 10
t = np.linspace(0,T,n + 1)
u = np.zeros(n + 1)
u[0] = 0
dt = T/n

for k in range(n):
    u[k + 1] = u[k] + dt*f(u[k],t[k])

plt.plot(t,u)
plt.show()

######################################  
