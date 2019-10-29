
import ODESolver
import numpy as np
import matplotlib.pyplot as plt

def f(u,t):
    return 0.1*u

g = lambda t: 0.2*np.exp(0.1*t)

for i in range(1,5):
    FE = ODESolver.ForwardEuler(f)
    FE.set_initial_condition(0.2)
    u, t = FE.solve(time_points = np.linspace(0,25,5*i))
    plt.plot(t,u)

t = np.linspace(0,25,50)
plt.plot(t,g(t),'k-',label='exact')
plt.legend()
plt.grid(True)
plt.show()
