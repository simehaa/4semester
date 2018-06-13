import numpy as np
import matplotlib.pyplot as plt

def du(u, t):
    return 1 - u**2 # differential equation (du/dx = 1 - x(t)**2)

def analytical(t):
    return (np.exp(2*t) - 1)/(np.exp(2*t) + 1) # analytical solution, solved by hand

def rk2(f, U0, T, n):   # f = differential equation, U0 = start, T = stop, n = steps)
    t = np.linspace(U0,T,n + 1) # t array (values along x axis)
    u = np.zeros(n + 1)         # u array (function values)
    u[0] = U0
    dt = T/float(n)
    for k in range(n):          # Runge-Kutta of 2nd order formulas
        K1 = dt*du(u[k],t[k])
        K2 = dt*du(u[k] + 0.5*K1, t[k] + 0.5*dt)
        u[k + 1] = u[k] + K2
    return t, u

# plot of results and absolute error to illustrate that Runge-Kutta2
# approaches function when the steplegth deacreases

x = np.linspace(0, 2, 50)
plt.plot(x, analytical(x), 'k-', label='analytical')

plt.plot(rk2(du, 0, 2, 2)[0],rk2(du, 0, 2, 2)[1], 'bo--', label='2 steps')
plt.plot(rk2(du, 0, 2, 4)[0],rk2(du, 0, 2, 4)[1], 'go--', label='4 steps')
plt.plot(rk2(du, 0, 2, 6)[0],rk2(du, 0, 2, 6)[1], 'ro--', label='6 steps')
plt.plot(rk2(du, 0, 2, 2)[0],abs(rk2(du, 0, 2, 2)[1] - analytical(rk2(du, 0, 2, 2)[0])), label='abs. error')
plt.plot(rk2(du, 0, 2, 4)[0],abs(rk2(du, 0, 2, 4)[1] - analytical(rk2(du, 0, 2, 4)[0])), label='abs. error')
plt.plot(rk2(du, 0, 2, 6)[0],abs(rk2(du, 0, 2, 6)[1] - analytical(rk2(du, 0, 2, 6)[0])), label='abs. error')
plt.title('Runge-Kutta of 2nd order with decreasing steplength, dx/dt = 1 - x(t)**2')
plt.xlabel('t')
plt.grid(True)
plt.legend(loc='best')
plt.show()

"""
simen@simen-VirtualBox:~/python/uke10$ python RungeKutta2_func.py
"""
