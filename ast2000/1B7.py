from __future__ import division
import numpy as np
from ast2000solarsystemviewer_v2 import AST2000SolarSystemViewer
import matplotlib.pyplot as plt
from math import sqrt

###################### seed and configuration ######################0
seed = 47566
system = AST2000SolarSystemViewer(seed)
np.random.seed(seed)
planetsRadius = system.radius
planetsMass = system.mass
planets_initial_x0 = system.x0
planets_initial_y0 = system.y0
planets_initial_vx0 = system.vx0
planets_initial_vy0 = system.vy0
rho0 = system.rho0
G = 4*np.pi**2
number_of_planets = system.number_of_planets
star_radius = system.star_radius
star_mass = system.star_mass
star_temperature = system.temperature
rho0 = system.rho0

def eulercromer(dt,T):

    """Initial planetPos and times"""
    n = int(T/dt)
    pos = np.zeros((2,number_of_planets,n))
    for j in range(number_of_planets):
            pos[0][j][0] = planets_initial_x0[j]
            pos[1][j][0] = planets_initial_y0[j]
    t = np.linspace(0,T,n)
    vx = planets_initial_vx0
    vy = planets_initial_vy0
    k = G*star_mass

    """Euler-Cromer, looping through time and planets"""
    for p in range(number_of_planets): # planets
        for i in range(n-1): # time
            x = pos[0,p,i]
            y = pos[1,p,i]
            r = sqrt(x**2 + y**2)
            if abs(y) < 1e-10:
                ay = 0
            else:
                ay = -k/float(r**2*sqrt(1 + abs(x**2/y**2))) * abs(y)/y
            if abs(x) < 1e-10:
                ax = 0
            else:
                ax = -k/float(r**2*sqrt(1 + abs(y**2/x**2))) * abs(x)/x
            vx[p] += ax*dt
            vy[p] += ay*dt
            pos[0,p,i + 1] = x + vx[p]*dt
            pos[1,p,i + 1] = y + vy[p]*dt

    return pos,t


def plot_orbits():
    pos,t = eulercromer(0.1,215)
    for p in range(number_of_planets):
        plt.plot(pos[0,p,:],pos[1,p,:],label='planet %i' % p)
    plt.grid(True)
    plt.axis([-60,60,-60,60])
    plt.plot(0,0,'ko',label='star')
    plt.xlabel('AU')
    plt.ylabel('AU')
    plt.legend(loc='best')
    plt.show()
    #system.orbit_xml(pos,t)

plot_orbits()
