import scipy.sparse.linalg as linalg
from matplotlib import animation
import matplotlib.pyplot as plt
import scipy.sparse as sparse
import scipy as sp
import numpy as np



x0      = 5                 #fm
a       = 0.7                 #fm
k       = 1.38              #1/fm

V0      = 3.4e7             #eV
delta_x = 14                #fm
mc_2    = 3.727e9           #eV
hbar    = 6.582e-16         #eVs
hbarc   = 1240/(2*np.pi)    #eVnm
c       = 2.998e23          #fm/s

A       = (2*np.pi*a**2)**(-0.25)
xp      = 10
x1      = 7.3               #fm
x2      = x1 + delta_x      #fm

Nt      = int(300)
Nx      = int(300)
T       = 1e-16             #s
t, dt   = np.linspace(0, T, Nt, retstep = True)
x, dx   = np.linspace(x1-xp, x2+xp, Nx, retstep = True)
i_x1    = np.abs(x-x1).argmin() + 1
i_x2    = np.abs(x-x2).argmin() + 1

def psi(x):
    return A*np.exp((-(x-x0)**2)/(4*a**2))*np.exp(1j*k*x)

def V(x):
    val = np.zeros_like(x)
    for n,i in enumerate(x):
        if x1 <= i <= x2:
            val[n] = V0
    return val

def animate(x, Psi):
    fig = plt.figure()
    plt.title("$\psi(x,t)$, $t \in$ [0,$10^{-16}$s], for $x > x_2, |\psi(x,t)|$ is scaled up by factor $10^{59}$")
    line , = plt.plot(x, Psi[0],'y-',label="$|\psi(x,t)|$")
    plt.plot([x1, x1], [0,1],'k--')
    plt.plot([x2, x2], [0,1],'k--', label="potensial barrier, $\Delta x$ = %2.f fm" % delta_x)
    plt.xlabel("x [fm]")
    plt.ylabel("|$\psi(x,t)$|")
    plt.legend(loc=2)
    plt.xlim(x1-xp,x2+xp)
    plt.ylim(-0.05,1)
    plt.draw()
    FPS = 30
    inter = 1e3/FPS

    def init():
        line.set_data([],[])
        return line ,

    def get_frame(frame):
        line.set_data(x,Psi[frame])
        return line ,

    anim = animation.FuncAnimation(fig,get_frame,init_func=init,frames=Nt,interval=inter,blit=True)
    anim.save('2f.gif',writer='imagemagick', fps=30)

    # plt.show()

I = sparse.identity(Nx)

c1 = (1j*(hbarc*c)/(2*mc_2))
data = np.ones((3, int(Nx)))
data[1,:] = -2
diags = [-1, 0, 1]
D = c1*sparse.spdiags(data, diags, Nx, Nx)/(dx**2)

c2 =-1j*c/hbarc
M = c2*sparse.spdiags(V(x), [0], Nx, Nx)

Psi = np.zeros((Nt, Nx), dtype = complex)
Psi[0] = psi(x)

for n,i in enumerate(t[1:]):
    A = (I - 0.5*dt*(D + M))
    b = (I + 0.5*dt*(D + M))*Psi[n]
    Psi[n+1] = linalg.spsolve(A, b)
    Psi[n+1] = Psi[n+1]/sp.integrate.simps(abs(Psi[n+1])**2, dx=dx)

psi = np.absolute(Psi)
psi[:,i_x2:] *= 1e59
animate(x, psi)
"""
t0 = 1e-18
i = np.abs(t-t0).argmin()
plt.title("t = %1.1g. For $x > x_2$, is $|\psi(x,t)|$ scaled up by factor $10^{59}$" % t0)
plt.plot([x1, x1], [0,1],'k--')
plt.plot([x2, x2], [0,1],'k--', label="potensial barrier, $\Delta x$ = %2.f fm" % delta_x)
plt.plot(x,psi[i],'y-',label="|$\psi(x,%1.1g)$|" % t0)
plt.xlabel("x [fm]")
plt.ylabel("|$\psi(x,%1.1g)$|" % t0)
plt.legend(loc=2)
plt.xlim(x1-xp,x2+xp)
plt.ylim(-0.05,1)
plt.show()"""
