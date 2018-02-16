import numpy as np
from matplotlib.pyplot import *
from matplotlib import animation


def wave(x,t):
    return 0.02*np.sin(x + t/(2*np.pi))

T = 10
dt = 1/60.
t = 0
nt = int(T/dt)
nx = 1001
x = np.linspace(-np.pi,np.pi,nx)
all_waves = []

while t < T:
    all_waves.append(wave(x,t))
    t += dt

fig = figure()
line , = plot(x,all_waves[0])
draw()
FPS = 60
inter = 1./FPS

def init():
    line.set_data([],[])
    return line ,

def get_frame(frame):
    line.set_data(x,all_waves[frame])
    return line ,

anim = animation.FuncAnimation(fig,get_frame,init_func=init,frames=nt,interval=inter,blit=True)

show()
