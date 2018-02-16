from __future__ import division
import numpy as np
from ast2000solarsystemviewer_v2 import AST2000SolarSystemViewer
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from math import sin, cos, sqrt, exp

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


def landing_probe(dt,T,angle,v0,planet,A):
    """dt and T, timestep and total time.
    0 < angle < pi/2, angle from tangential to vertically straight down
    v0 in km/s absolute value.
    planet, integer for planets index
    A, area of parachute
    everything done in SI-units"""
    m_planet = planetsMass[planet]*1.99e30 # kg
    r_planet = planetsRadius[planet]*1000 # m
    h = 40000000. # m
    m_probe = 100. # kg
    n = int(T/dt)
    pos = np.zeros((n,2),dtype=float)
    pos[0][1] = r_planet + h # pos[0,0] = 0
    t = np.linspace(0,T,n)
    vx = v0*cos(angle)   # m/s
    vy = - v0*sin(angle) # m/s
    Fd_coeff = 0.5*rho0[planet]*A
    g_surface = 6.67e-11*m_planet/r_planet**2
    print "gravity at surface=%.2f m/s**2, atmosphere density at surface=%.2f kg/m**3" % (g_surface,rho0[planet])
    h_scale = 75200./g_surface
    def fd(h,vx,vy):
        return Fd_coeff*(vx**2 + vy**2)*exp(-h/h_scale)
    def gr(r_squared):
        return 6.67e-11*m_planet/r_squared

    for i in range(n - 1): # time
        x = pos[i,0]
        y = pos[i,1]
        h = sqrt(x**2 + y**2) - r_planet
        f = fd(h,vx,vy)
        g = gr(x**2 + y**2)
        if h <= 0:
            v_radial = (vx*x + vy*y)/sqrt(x**2 + y**2)
            if abs(v_radial) < 3:
                print "landing probe landed safely, after %.1f seconds" % (i*dt)
            else:
                print "landing probe crashed with the planets surface with to high velocity"
            pos[i:,0].fill(x)
            pos[i:,1].fill(y)
            break
        if f > 25000:
            print "landing probe ripped apart due to friction forces"
            break

        if abs(x) < 1e-16:
            gx = 0
        else:
            gx = - g/sqrt(1 + y**2/x**2) * abs(x)/x
        if abs(vx) < 1e-16:
            fx = 0
        else:
            fx = - f/sqrt(1 + vy**2/vx**2) * abs(vx)/vx
        if abs(y) < 1e-16:
            gy = 0
        else:
            gy = - g/sqrt(1 + x**2/y**2) * abs(y)/y
        if abs(vy) < 1e-16:
            fy = 0
        else:
            fy = - f/sqrt(1 + vx**2/vy**2) * abs(vy)/vy

        ax = fx/m_probe + gx
        ay = fy/m_probe + gy
        vx += ax*dt
        vy += ay*dt
        pos[i+1][0] = x + vx*dt
        pos[i+1][1] = y + vy*dt

    return pos,t

def plot_landing():
    dt = 20
    T = 10000000
    angle = np.pi/4.#np.pi/4.
    v0 = 2236. # m/s
    planet = 1
    A = 12 # m**2
    pos,t = landing_probe(dt,T,angle,v0,planet,A)
    x = pos[:,0]*0.001
    y = pos[:,1]*0.001
    plt.plot(x,y,'k--')
    plt.xlabel('km')
    plt.ylabel('km')
    plt.grid()
    plt.axis([-3e4,3e4,-1e4,5e4])

    circle = Circle((0,0),planetsRadius[planet])
    fig = plt.gcf()
    ax = fig.gca()
    ax.add_artist(circle)

    # system.landing_sat(pos,t,1)
    plt.show()

plot_landing()

"""
[Command: python -u /home/simen/ast2000/1B8.py]
gravity at surface=6.82 m/s**2, atmosphere density at surface=0.95 kg/m**3
landing probe landed safely, after 21648.3 seconds
"""
