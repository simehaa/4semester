import numpy as np
import matplotlib.pyplot as plt
from math import sqrt, cos

# Runge-Kutta method of 4th order
def rk(xStart,vStart,tStart):
    a1 = diffEq(xStart,vStart,tStart)
    v1 = vStart
    xHalf1 = xStart + v1 * dt/2.0
    vHalf1 = vStart + a1 * dt/2.0
    a2 = diffEq(xHalf1,vHalf1,tStart+dt/2.0)
    v2 = vHalf1
    xHalf2 = xStart + v2 * dt/2.0
    vHalf2 = vStart + a2 * dt/2.0
    a3 = diffEq(xHalf2,vHalf2,tStart+dt/2.0)
    v3 = vHalf2
    xEnd = xStart + v3 * dt
    vEnd = vStart + a3 * dt
    a4 = diffEq(xEnd,vEnd,tStart + dt)
    v4 = vEnd
    aMiddle = 1.0/6.0 * (a1 + 2*a2 + 2*a3 + a4)
    vMiddle = 1.0/6.0 * (v1 + 2*v2 + 2*v3 + v4)
    xEnd = xStart + vMiddle * dt
    vEnd = vStart + aMiddle * dt
    return xEnd, vEnd

# differential equation, inhomgoenous and of second degree (homogenous if F = 0)
def diffEq(xNow,vNow,tNow):
    return (F*cos(w*tNow) - b*vNow - k*xNow)/m

# a function that uses rk and diffeq functions to solve for the entire motion
def solve():
    n = int(T/dt)
    x = np.zeros(n)
    v = np.zeros(n)
    t = np.linspace(0,T,n)
    x[0] = x0
    v[0] = v0
    for i in range(n - 1):
        x[i + 1],v[i + 1] = rk(x[i],v[i],t[i])
    return x,v,t


# oppgave 4a)
T = 5; dt = 0.01; m = 0.1; b = 0.1; k = 10.; F = 0; w = sqrt(k/m); x0 = 0.1; v0 = 0
x,v,t = solve()
plt.plot(t,x,label='numerisk')
plt.xlabel('time [s]')
plt.ylabel('position [m]')
y = b/(2*m)
plt.plot(t,np.exp(-y*t)*x0*np.cos(w*t),'--',label='analytisk')
plt.legend()
plt.grid(True)
plt.show()

# oppgave 4b)
T = 5; dt = 0.01; m = 0.5; k = 10.; F = 0; w = sqrt(k/m); x0 = 0.1; v0 = 0
B = [sqrt(k*m)*0.5,sqrt(k*m)*2,sqrt(k*m)*8]
string = ['Underk','K','Overk']
for j in range(3):
    b = B[j]
    x,v,t = solve()
    plt.plot(t,x,label='%sritisk' % string[j])
plt.xlabel('time [s]')
plt.ylabel('position [m]')
plt.legend()
plt.grid(True)
plt.show()

# oppgave 4c)
def plot_position(t,x):
    plt.plot(t,x)
    plt.xlabel('time [s]')
    plt.ylabel('position [m]')
    plt.grid(True)
    plt.show()
T = 3; dt = 0.001; m = 0.1; b = 0.04; k = 10.; F = 0.1; w = sqrt(k/m); x0 = 0.1; v0 = 0
x,v,t = solve()
plot_position(t,x)
T = 3; dt = 0.001; m = 0.005; b = 0.02; k = 20.; F = 12; w = sqrt(k/m); x0 = 0.1; v0 = 0
x,v,t = solve()
plot_position(t,x)
T = 3; dt = 0.001; m = 0.1; b = 0.5; k = 2000.; F = 700; w = 0.9*sqrt(k/m); x0 = 0.1; v0 = 1.
x,v,t = solve()
plot_position(t,x)

# oppgave 4d) og oppgave 7
T = 3; dt = 0.01; m = 0.005; b = 0.02; k = 20.; F = 12; x0 = 0.1; v0 = 1.
N = 500
W = np.linspace(0.75,1.25,N)
Emax = np.zeros(N)
for i in range(N):
    w = W[i]*sqrt(k/m)
    x,v,t = solve()
    Emax[i] = 0.5*k*np.max(x)**2
plt.plot(W,Emax)
plt.xlabel('relative frequency to w0')
plt.ylabel('E_max')
plt.grid(True)

# finding delta_w from Emax/2 :
Emax_2 = np.max(Emax)*0.5
emax_left, emax_right = np.split(Emax,2)
i_left = (np.abs(emax_left-Emax_2)).argmin()
i_right = (np.abs(emax_right-Emax_2)).argmin() + int(N*0.5)
delta_w = W[i_right] - W[i_left]

# plot of Emax vs W, including two end points of delta_w at Emax/2
plt.title('delta w (w-distance between red and green dot) = %.3f' % delta_w)
plt.plot(W[i_left],Emax[i_left],'go',W[i_right],Emax[i_right],'ro')
plt.show()

i_emax = (np.abs(Emax-np.max(Emax))).argmin()
Q1 = W[i]/delta_w
Q2 = sqrt(m*k)/b
print "Q factor from graph, w0/dw = %.2f" % Q1
print "Q factor from sqrt(m*k)/b  = %.2f" % Q2

"""
[Command: python -u /home/simen/UiO_simehaa/V2018/fys2130/RK4.py]
Q factor from graph, w0/dw = 16.41
Q factor from sqrt(m*k)/b  = 15.81
[Finished in 3.916s]
"""
