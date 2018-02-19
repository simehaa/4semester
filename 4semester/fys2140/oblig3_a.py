import numpy as np
from math import sqrt
from matplotlib.pyplot import *
from matplotlib import animation

k1 = 0.6
k2 = 0.7
w1 = sqrt(k1 + 1)
w2 = sqrt(k2 + 1)

def wave(x,t):
    return np.sin(x*k1 - w1*t) + np.sin(x*k2 - w2*t)

T = 20
dt = 1/60.
t = 0
nt = int(T/dt)
nx = 1001
x = np.linspace(0,100,1001)
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
