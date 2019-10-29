from math import pi, log

def egg(M,To=20,Ty=70):
    """this is the formula for the time
    it takes to cook the perfect egg, where M
    is the mass, To is start temp and Ty is
    desired temp in the core of the egg"""
    c = 3.7
    K = 5.4e-3
    rho = 1.038
    Tw = 100.0

    time = (M**(2.0/3.0)*c*rho**(1.0/3.0))/ \
    (K*pi**2*(4*pi/3)**(2.0/3.0))*log(0.76*(To-Tw)/(Ty-Tw))

    return time

Ty = [60,70]
M  = [47,67]
To = [4, 25]

for m in M:
    for ty in Ty:
        for to in To:
            time = egg(m,To=to,Ty=ty)
            print "With mass %2g g and initial temperature %2g C,\
 final core temperature %2g C is reached after \
%2.f seconds" % (m, ty, to, time)
