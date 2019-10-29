import numpy as np
import matplotlib.pyplot as plt

def f(u,t):
    return 0.1*u

def g(t):
    return 0.2*np.exp(0.1*t)

def FE(f, U0, T, n):
    t = np.linspace(0,T,n+1)
    y = np.zeros(n+1)
    y[0] = 0.2
    dt = T/float(n)
    for k in range(n):
        y[k + 1] = y[k] + f(y[k],0)*dt
    return y, t

for i in range(1,5):
    t = FE(f, 0.2, 25, 5*i)[1]
    y = FE(f, 0.2, 25, 5*i)[0]
    plt.plot(t,y,'--')
t = np.linspace(0,25,50)
plt.plot(t,g(t),'k-',label='exact')
plt.legend()
plt.grid(True)
plt.show()
