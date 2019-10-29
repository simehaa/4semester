from math import exp, cos, pi
f = StringFunction('exp(-a*x)*cos(w*t)'
                   independent_variables=['t']
                   a=1, w=pi, x=2)
print f
