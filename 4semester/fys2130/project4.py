from project import differential
from math import sqrt,cos
import numpy as np
import matplotlib.pyplot as plt

def diffEq(xNow,vNow,tNow):
    return (Fd*cos(wd*tNow) - k*xNow)/m

plot_str = r'$m\ddot{x}(t) + kx(t) = F_D cos(\omega t)$'
m = 0.500
k = 1.0
Fd = 0.7
w0 = sqrt(k/m)
oppgave4 = differential(diffEq,plot_str,T = 200,x0=2.0)
omegas = [13.0/8.0*w0, 2.0/(sqrt(5) - 1)*w0]
titles = [r'$13/8 \cdot \omega_0$',r'$2/(\sqrt{5} - 1) \cdot \omega_0$']
t = np.linspace(0,40,1001)

for wd,st in zip(omegas,titles):
    C = 2 - (Fd/(m*(w0**2 - wd**2)))
    x =     (Fd/(m*(w0**2 - wd**2)))*np.cos(wd*t) + C*np.cos(w0*t)
    v = -wd*(Fd/(m*(w0**2 - wd**2)))*np.sin(wd*t) - w0*C*np.sin(w0*t)
    oppgave4.solve()
    plt.title(r'$m\ddot{x}(t) + kx(t) = F_D \cos{(\omega_D t)}$, where $\omega_D$ = ' + st)
    plt.plot(oppgave4.x,oppgave4.v,'r-',label='numerical')
    # plt.plot(x,v,'y--',label='analytical')
    plt.legend()
    plt.grid()
    plt.xlabel('position [m]')
    plt.ylabel('velocity [m/s]')
    plt.show()

"""
[Command: python -u /home/simen/github/university/4semester/fys2130/project4.py]
[Finished in 55.372s]
"""
