import numpy as np
from matplotlib.pyplot import *
from matplotlib import animation


def animate(u,x):
    fig = figure()
    line, = plot(x,u[:,0])
    draw()
    FPS = 60

    def init():
        line.set_data([],[])
        return line,
    def get_frame(frame):
        line.set_data(x,u[:,frame])
        return line,

    anim = animation.FuncAnimation(fig,get_frame,init_func=init,frames=u.shape[1],interval=1e3/FPS,blit=True)
    grid()
    ylim(1.2*np.min(u),1.2*np.max(u))
    show()


def time_loop(u,k):
    f = 2*(1 - k) # factor for efficiency in loop
    nt = u.shape[1]
    for j in range(1,nt - 1):
        # inner position values
        u[1:-1,j + 1] = f*u[1:-1,j] - u[1:-1,j - 1] + k*(u[2:,j] + u[:-2,j])
        # first and last position
        u[0   ,j + 1] = f*u[0   ,j] - u[0   ,j - 1] + k* u[1 ,j]
        u[-1  ,j + 1] = f*u[-1  ,j] - u[-1  ,j - 1] + k* u[-2,j]
    return u


def wave(form='gaussian',A=1,dt=0.1,nx=401,nt=600,v=0.5,length=40., \
              sigma=5.,derivation_factor=1,num_standing_waves=3):
    # creation of wave including the two first timesteps
    u = np.zeros((nx,nt))
    t = np.arange(0,nt,dt)
    x = np.linspace(-length/2.,length/2.,nx)
    dx = length/(nx - 1)
    if form == 'gaussian':
        u_init = A*np.exp(-(x/(2*sigma))**2)
    elif form == 'sin':
        u_init = np.sin(x*num_standing_waves*2*np.pi/length)
    dudt = derivation_factor*v*x*u_init/(2*sigma**2)
    u[:,0] = u_init - dt*dudt
    u[:,1] = u_init
    k = (dt*v/dx)**2
    u1 = time_loop(u,k)
    return u1,x

# setter derivation_factor lik
# a) - 1
# b) 0.5
# c) 2.0
# setter form lik
# d) 'sin'
u,x = wave()
animate(u,x)

"""
[Command: python -u /home/simen/github/university/4semester/fys2130/oblig5.py]
[Finished in 2.728s]
"""
