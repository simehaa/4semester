from project import differential
from math import sqrt,cos

def diffEq(xNow,vNow,tNow):
    return (Fd*cos(w*tNow) - b*vNow - k*xNow)/m

plot_str = r'$m\ddot{x}(t) + b\dot{x}(t) + kx(t) = F_D cos(\omega t)$'
m = 0.500
k = 1.0
b = 0.1
Fd = 4# 0.7
w0 = sqrt(k/m)
w = 13.0/8.0*w0
oppgave5 = differential(diffEq,plot_str,T = 100,x0 = 2.0,v0 = 2.)
oppgave5.solve()
oppgave5.plot()

"""
[Command: python -u /home/simen/github/university/4semester/fys2130/project5.py]
[Finished in 20.599s]
"""
