'''
mp = 1.6737e-27
h = 6.63e-34
c = 299792458.
me = 9.11e-31

for l in [656.2,486.1,434.0]:
    print (c + (h/(l*1e-9*mp)))/c - 1

print me*mp/(me + mp), me
'''
from math import sqrt, atan, pi

L = 25e-6
C = 100e-9
w0 = 1/(sqrt(L*C))
R = 1.
Q = sqrt(L/(R**2*C))
print Q
dw = 1/(2*Q*sqrt(L*C))
print dw
wF = w0 + dw
phi = ((w0**2 - wF**2)/(wF*R/L))**(-1)
s = (atan(phi))
print s/pi, "pi"
