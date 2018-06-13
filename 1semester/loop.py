print '----------------'
C = -20
dC = 5
while C <= 40:
    F = (9.0/5)*C + 32
    print ' %.1f %.1f' % (C, F)
    C = C + dC
print '----------------'
x = 1.2
N = 25
k = 1
s = x
sign = 1.0
import math

while k < N:
    sign = - sign
    k = k + 2
    term = sign*x**k/math.factorial(k)
    s = s + term

print 'sin(%g) = %g (approximation with %d terms)' % (x, s, N)
print '----------------'
