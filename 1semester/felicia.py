"""
u[k+1]=u[k] + K[2]
#where
K[1]= dt*f(u[k], dt)
K[2]= dt*f(u[k]+0.5*K[1], t[k]+ 0.5*dt)
#with
dt= t[k+1]-t[k]
"""
import numpy as np


def RungeKutta2(f, U0, T, n):
    t= np.linspace(U0,T,n+1)
    u= np.zeros(n+1)

    u[0]= U0
    t[0]= 0

    dt= T/float(n)
    for k in range(n):

        K1= dt*f(u[k], dt)
        K2= dt*f(u[k]+0.5*K1, t[k]+ 0.5*dt)

        u[k+1]= u[k] + K2

    return u, t


def f(u, t):
    return u

import numpy as np
import matplotlib.pyplot as plt

u, t = RungeKutta2(f, 1, 4, 40)

plt.plot(t, u, c="b")
t_exact= np.linspace(0, 4, 100)
u_exact= np.exp(t_exact)
plt.plot(t_exact, u_exact, c="r")
plt.show()

"""
simen@simen-VirtualBox:~/python/uke10$ python RungeKutta2_func.py
"""
