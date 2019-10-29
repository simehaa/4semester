# Exercise 1.11: Compute the air resistance on a football
from math import pi
# The variables:
Cd = 0.4        # drag coefficient
q  = 1.2        # kg/m**3 (the density of air)
r  = 0.11       # m (radius of the ball)
A  = pi*r**2    # m**2 (the cross-sectional area)
V1 = 120.0/3.6  # m/s (*3.6 for km/h conversion) hard kick
V2 = 30.0/3.6   # m/s (*3.6 for km/h conversion) soft kick
m  = 0.43       # kg (mass)
g  = 9.81       # m/s**2 (the gravitational acceleration on Earth)
Fg = m*g        # kg*m/s**2 (Newton)

Fd1 = (1.0/2)*Cd*q*A*V1**2  # the drag force for the hard kick
Fr1 = Fd1/Fg                # the force ratio for the hard kick
Fd2 = (1.0/2)*Cd*q*A*V2**2  # the drag force for the soft kick
Fr2 = Fd2/Fg                # the force ratio for the soft kick

print """Drag force on a kicked ball

Hard kick
Drag force         = %.1f Newton
Speed              = %.1f m/s
Ratio between drag
force and gravity  = %.1f

Soft kick
Drag force         = %.1f Newton
Speed              = %.1f m/s
Ratio between drag
force and gravity  = %.1f""" % (Fd1, V1, Fr1, Fd2, V2, Fr2)

"""
simen@simen-VirtualBox:~/python/uke1$ python kick.py
Drag force on a kicked ball

Hard kick
Drag force         = 10.1 Newton
Speed              = 33.3 m/s
Ratio between drag
force and gravity  = 2.4

Soft kick
Drag force         = 0.6 Newton
Speed              = 8.3 m/s
Ratio between drag
force and gravity  = 0.2
"""
