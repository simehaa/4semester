from project import differential
from math import sqrt,cos
import matplotlib.pyplot as plt

def diffEq(xNow,vNow,tNow):
    m = 0.00001 + psi*tNow # time dependent mass
    return g - ((b + psi)*vNow + k*xNow)/m

plot_str = 30*' ' + r'$\dot{m}(t) = \psi$' \
+ '\n' + r'$m(t)\ddot{x}(t) + (b+\psi)\dot{x}(t) + kx(t) = m(t)g$'
k = 0.475
b = 0.001
g = 9.81
psi = 0.00055
oppgave6 = differential(diffEq,plot_str,dt=0.0001,T=3,x0=0.001,v0=0.001)
x,v,t = oppgave6.solve()
oppgave6.plot()

plt.plot(t,x,label='position')
plt.xlabel('time [s]')
plt.ylabel('position [m]')
plt.grid()
plt.legend()
plt.show()

"""
[Command: python -u /home/simen/github/university/4semester/fys2130/project6.py]
[Finished in 91.705s]
"""
