import ODESolver #file from book files, saved in same folder
import numpy as np
import matplotlib.pyplot as plt

epsilon = 0.001

def f(t, y):
    return 1./(2*(t - 1)) # differential equation

exact = lambda x: 1 + np.sqrt(x + epsilon) # analytical solution

for i in range(2,7):
    k = 2**i # generates, 4, 8, 16, 32, 64

    FE = ODESolver.ForwardEuler(f) # method from ODESolver.py file
    FE.set_initial_condition(1 + np.sqrt(epsilon))

    RK4 = ODESolver.RungeKutta4(f)
    RK4.set_initial_condition(U0 = 1 + np.sqrt(epsilon))

    u0, t0 = FE.solve(time_points = np.linspace(0,4,k))
    u1, t1 = RK4.solve(time_points = np.linspace(0,4,k))

    plt.plot(t0, u0,'o--',label='FE: %i steps' % k)
    plt.plot(t1, u1,'o--',label='RK4: %i steps' % k)

x = np.linspace(0,4,51) # exact solution array
plt.plot(x,exact(x), 'k-',label='exact') # exact plot
plt.legend(loc='best')
plt.grid(True)
plt.show()
# the plot showed that Runge-Kutta4 was much better than
# ForwardEuler, and 64 steps was a sufficient approximation

"""
simen@simen-VirtualBox:~/python/uke10$ python yx_ODE_FE_vs_RK4.py
"""
