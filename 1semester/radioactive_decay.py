import numpy as np
import matplotlib.pyplot as plt

# a)
class Decay:
    def __init__(self, a):
        self.a = a

    def __call__(self, u):
        return -self.a*u

# b)
a = np.log(2)/5600. # 1/y
f = Decay(a)     # instance of class

# c)
T = 20000        # years
dt = 500         # steplength 500 years
n = T/dt         # values
t = np.linspace(0,20000,n + 1)
u = np.zeros(n + 1) # empty array for ForwardEuler
e = np.zeros(n + 1) # empty array for exact solution
u[0] = e[0] = 1  # initial condition, 1 to illustrate 100 percent

for k in range(n):
    u[k + 1] = u[k] + dt*f(u[k]) # ForwardEuler
    e[k + 1] = np.exp(-a*t[k + 1])  # exact

plt.plot(t,u, label='differentiation')
plt.plot(t,e, label='exact')
plt.xlabel('years')
plt.ylabel('fraction of particles that remains radioactive')
plt.title('radioactive decay')
plt.legend()
plt.grid(True)
plt.show()

# the ForwardEuler looks very much, yet not quite alike the exact solution
"""
simen@simen-VirtualBox:~/python/uke10$ python radioactive_decay.py
"""
