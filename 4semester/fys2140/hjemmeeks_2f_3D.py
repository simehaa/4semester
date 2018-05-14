import scipy.sparse.linalg as linalg
from matplotlib import animation
import matplotlib.pyplot as plt
import scipy.sparse as sparse
import scipy as sp
import numpy as np
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation
import imageio

x0      = 5                 #fm
a       = 0.7                 #fm
k       = 1.38              #1/fm

V0      = 3.4e7             #eV
delta_x = 25                #fm
mc_2    = 3.727e9           #eV
hbar    = 6.582e-16         #eVs
hbarc   = 1240e6/(2*np.pi)  #eVnm
c       = 2.998e20          #fm/s

A       = (2*np.pi*a**2)**(-0.25)
xp      = 10
x1      = 7.5               #fm
x2      = x1 + delta_x      #fm

Nt      = 10
Nx      = int(1e3)
T       = 1e-18             #s
t, dt   = np.linspace(0, T, Nt, retstep = True)
x, dx   = np.linspace(x1-xp, x2+xp, Nx, retstep = True)

def psi(x):
    return A*np.exp((-(x-x0)**2)/(4*a**2))*np.exp(1j*k*x)

def V(x):
    val = np.zeros_like(x)
    for n,i in enumerate(x):
        if x1 <= i <= x2:
            val[n] = V0
    return val

def animate(x, Psi):
    nt = len(x)
    fig = plt.figure()
    plt.title("$\Psi(x,t)$, $t \in$ [0,$10^{-18}$s]")
    line , = plt.plot(x, Psi[0],'y-',label="$\Psi(x,t)$")
    plt.plot([x1, x1], [-1,1],'k--')
    plt.plot([x2, x2], [-1,1],'k--', label="potensial barrier, $\Delta x$ = %2.f fm" % delta_x)
    plt.xlabel("x [fm]")
    plt.legend(loc=2)
    plt.xlim(np.min(x),np.max(x))
    plt.draw()
    FPS = 30
    inter = 1e3/FPS

    def init():
        line.set_data([],[])
        return line ,

    def get_frame(frame):
        line.set_data(x,Psi[frame])
        return line ,

    anim = animation.FuncAnimation(fig,get_frame,init_func=init,frames=nt,interval=inter,blit=True)
    plt.show()

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

for n,i in enumerate(t[:-1]):
    A = (I - 0.5*dt*(D + M))
    b = (I + 0.5*dt*(D + M))*Psi[n]
    Psi[n+1] = linalg.spsolve(A, b)
    Psi[n+1] = Psi[n+1]/sp.integrate.simps(abs(Psi[n+1])**2, dx=dx)

filenames = []
fig = plt.figure()
ax = p3.Axes3D(fig)
for i in range(Nt):
    ax.plot(x,Psi.real[:,0],Psi.imag[:,0])
    ax.set_xlim3d([np.min(x), np.max(x)])
    ax.set_xlabel('x [fm]')

    ax.set_ylim3d([-0.3, 0.3])
    ax.set_ylabel('Real')

    ax.set_zlim3d([-0.3, 0.3])
    ax.set_zlabel('Imaginary')
    plt.savefig('/github/university/4semester/fys2140/im%i' % i + '.jpg')
    filenames.append('/github/university/4semester/fys2140/im%i' % i + '.jpg')


images = []
for filename in filenames:
    images.append(imageio.imread(filename))
imageio.mimsave('/github/university/4semester/fys2140/movie.gif', images)

# Attaching 3D axis to the figure


data = []
for n in range(Nx):
    A = np.empty((3,Nt))
    A[0,:] = x[n]
    A[1,:] = Psi.real[:,n]
    A[2,:] = Psi.imag[:,n]
    data.append(A)

lines = [ax.plot(dat[0, 0:1], dat[1, 0:1], dat[2, 0:1])[0] for dat in data]



# Setting the axes properties
