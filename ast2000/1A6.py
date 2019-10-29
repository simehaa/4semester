from __future__ import division
import numpy as np
from ast2000solarsystemviewer_v2 import AST2000SolarSystemViewer

###################### seed and configuration ######################0
seed = 47566
system = AST2000SolarSystemViewer(seed)
np.random.seed(seed)
planetsRadius = system.radius            # km
planetsMass = system.mass                # solar masses
planets_initial_x0 = system.x0           # AU
planets_initial_u0 = system.y0           # AU
planets_initial_vx0 = system.vx0         # AU
planets_initial_vy0 = system.vy0         # AU
rho0 = system.rho0                       # kg/m**3
G = 4*np.pi**2                           # gravitational constant in AU
number_of_planets = system.number_of_planets
star_radius = system.star_radius         # km
star_mass = system.star_mass             # solar masses
star_temperature = system.temperature    # K
############################## values ##############################
N = 100000                               # particles in one box
k = 1.38064852e-23                       # Boltzmann's constant
T = 10000                                  # K
m_H2 = 1.6737236e-27*2                   # kg
m_satelite = 1000                        # kg
L = 1e-6                                 # m
sigma = np.sqrt(k*T/m_H2)                # standard deviation
y = 6.67e-11                             # gamma, gravity constant
dt = 1e-12                               # s
t = 1e-9                                 # s
####################################################################


def escapevelocity():
    M = planetsMass[0]*1.99e30          # kg
    R = planetsRadius[0]*1000           # m
    return np.sqrt(2*y*M/R)             # m/s


def engine(N,T):
    pos = np.random.uniform(-L/2,L/2,(N,3))  # position matrix
    vel = np.random.normal(0,sigma,(N,3))    # velocity matrix
    combustion    = np.zeros(3); combustion[2].fill(L/2) # replacement of escaped particles
    abs_v         = np.sqrt(vel[:,0]**2 + vel[:,1]**2 + vel[:,2]**2)
    Ek_numerical  = np.sum(abs_v**2)*0.5*m_H2/N # mean kinetic energy
    Ek_analytical = 3*k*T/2                  # analytical kinetic energy
    v_a           = np.sqrt(8*k*T/(np.pi*m_H2))
    v_n           = np.sum(abs_v)/N
    v_z_floor     = 0
    counter_floor = 0
    v_z_hole      = 0
    counter_hole  = 0
    for i in range(int(t/dt)):
        pos += vel*dt # Euler's method
        # next two lines are for keeping particles in the box
        condition_wall = abs(pos) > L/2 # returns True for all indices where particle is outside of the box
        vel[condition_wall] *= -1       # switching velocity for those indices (in respectively x,y,z direction)

        # next three lines are for counting and computing pressure left on the floor side
        condition_floor = pos[:,2] < -L/2
        counter_floor  += np.sum(condition_floor)
        v_z_floor      += np.sum(abs(vel[:,2][condition_floor]))

        # next three lines are for counting and summarizing velocities out of the hole in the bottom
        condition_hole  = np.logical_and(abs(pos[:,0]) < L/4, np.logical_and(abs(pos[:,1]) < L/4, pos[:,2] < -L/2))
        v_z_hole       += np.sum(abs(vel[:,2][condition_hole]))
        counter_hole   += np.sum(condition_hole)

        # replacing those particles whom escaped in the top of the box
        pos[condition_hole] = combustion
    momentum_floor      = v_z_floor*m_H2*2 # kg m/s
    force_floor         = momentum_floor/t # N
    pressure_numerical  = force_floor/L**2 # Pa
    pressure_analytical = k*T*N/L**3       # Pa
    momentum_hole       = v_z_hole*m_H2    # kg m/s

    # escape velocity within 20 mins
    full_launch_time = 20*60 # s
    n_boxes = m_satelite*escapevelocity()*t/(full_launch_time*momentum_hole)
    fuel = n_boxes*m_H2*full_launch_time*(counter_hole/t)
    return Ek_analytical, Ek_numerical, pressure_analytical, pressure_numerical, \
           v_a, v_n, n_boxes, fuel, momentum_hole


def launch_with_fuel_and_gravity(fuel,momentum_hole,boxes):
    t         = 20*60 # s
    dt        = 0.01  # s
    m_start   = 1000 + fuel # kg
    F_thrust  = momentum_hole*boxes/1e-9 # Newtons
    a_gravity = - y*planetsMass[0]*1.99e30/(planetsRadius[0]*1000)**2 # m/s**2 radiant direction out from planet (gravity on surface used)
    timesteps = int(t/dt)
    fuelloss  = fuel/timesteps
    print "g = %f" % a_gravity
    v = 0
    for i in range(timesteps):
        m_rocket = m_start - i*fuelloss
        a = F_thrust/m_rocket + a_gravity
        v += a*dt
    return v


if __name__ == '__main__':
    Ek_a,Ek_n,p_a,p_n,v_a,v_n,boxes,fuel,momentum_hole = engine(N,T)
    print "Escapevelocity             = %5.f m/s"  % escapevelocity()
    print "Analytical kinetic energy  = %.4g J"    % Ek_a
    print "Numerical  kinetic energy  = %.4g J"    % Ek_n
    print "Analytical mean velocity   = %5.f m/s"  % v_a
    print "Numerical  mean velocity   = %5.f m/s"  % v_n
    print "Analytical pressure        = %.4g Pa"   % p_a
    print "Numerical  pressure        = %.4g Pa"   % p_n
    print "Amount of boxes            = %.4g"      % boxes

    print "\nSatelite only (fuel mass excluded)"
    print "Fuel needed                = %.4g kg"   % fuel
    v_launch = launch_with_fuel_and_gravity(fuel,momentum_hole,boxes)
    print "velocity after 20 mins     = %.4g m/s\n\n"  % v_launch

    print "Scaled up mass of fuel and amount of boxes by factor 2.5"
    factor = 50.
    boxes *= factor
    fuel  *= factor
    v_launch = launch_with_fuel_and_gravity(fuel,momentum_hole,boxes)
    print "velocity after 20 mins    = %5.f m/s"  % v_launch
    print "total weight at launch    = %4.f kg" % (fuel + 1000)
    print "new amount of boxes       = %.4g" % boxes

"""
[Command: python -u /home/simen/ast2000/1A6.py]
Escapevelocity             = 13512 m/s
Analytical kinetic energy  = 2.071e-19 J
Numerical  kinetic energy  = 2.067e-19 J
Analytical mean velocity   = 10248 m/s
Numerical  mean velocity   = 10229 m/s
Analytical pressure        = 1.381e+04 Pa
Numerical  pressure        = 1.468e+04 Pa
Amount of boxes            = 4.947e+12

Satelite only (fuel mass excluded)
Fuel needed                = 1579 kg
velocity after 20 mins     = 8108 m/s

Scaled up mass of fuel and amount of boxes by factor 2.5
velocity after 20 mins    = 13684 m/s
total weight at launch    = 4946 kg
new amount of boxes       = 1.237e+13
[Finished in 4.357s]
"""
