a = 2; b = 1; c = 2
from cmath import sqrt # must use cmath module to take negative squareroots
q = b*b - 4*a*c
q_sr = sqrt(q)
x1 = (-b + q_sr)/2*a
x2 = (-b - q_sr)/2*a
print x1, x2
