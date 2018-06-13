me = 9.1094e-31 # kg - mass of an electron
e  = 1.6022e-19 # C - the elementary charge
e0 = 8.8542e-12 # C**2*s**2/(kg*m**3) - the electrical permitivity of vacuum
h  = 6.6261e-34 # Js
n  = 1
print """An electron in a Hydrogen atom in the
n-th level has the energy:"""
while n <= 20:
    En = - me*e**4/(8*e0**2*h**2)*1/n**2
    print '%5i   =   %7.4g J' % (n, En)
    n += 1
f = float(1)
i = float(1)
print """Energy released when an
electron moves from _ to _"""
while f <= 5:
    D = me*e**4/(8*e0**2*h**2)*(1./i**2 - 1./f**2)
    print '%5i -> %i = %1.4g J' % (i, f, D)
    f += 1
