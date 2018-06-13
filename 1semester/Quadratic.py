# 7.5
from numpy.lib.scimath import sqrt

class Quadratic:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def value(self, x): # funcion value at a point x
        return self.a*x**2 + self.b*x + self.c

    def table(self, n, interval): # table of 'x' and 'f(x)' with n points in the interval [L,R]
        L = interval[0]; R = interval[1]
        dx = (R - L)/float(n - 1)
        for i in range(n):
            x = L + i*dx
            f = self.a*x**2 + self.b*x + self.c
            print '%.2f  %.2f' % (x, f)

    def roots(self):
        return (-self.b + sqrt(self.b**2 - 4*self.a*self.c))/(2.*self.a),\
               (-self.b - sqrt(self.b**2 - 4*self.a*self.c))/(2.*self.a)

# test functions

def test_value():
    # a=1 b=2 c=-15 and x=3
    x = 3
    expected = 1*x**2 + 2*x - 15
    quad = Quadratic(1,2,-15)
    computed = quad.value(x)
    tol = 1e-14
    success = abs(expected - computed) < tol
    msg = 'value fail! expected: %.2f class computation: %.2f' % (expected, computed)
    assert success, msg

test_value()

def test_roots(): # test function for two real roots
    tol = 1e-14
    # a=1 b=1 c=-6
    exp_0 = 2 # solutions solved by hand
    exp_1 = -3
    quad = Quadratic(1,1,-6)
    com_0 = quad.roots()[0]
    com_1 = quad.roots()[1]
    success = abs(exp_0 - com_0) < tol and abs(exp_1 - com_1) < tol
    msg = 'failed! expected roots: %.f, %.f got %.f, %.f' % (exp_0, exp_1, com_0, com_1)
    assert success, msg

test_roots()

"""
simen@simen-VirtualBox:~/python/uke9$ python Quadratic.py
"""
