# 9.3
from math import *

class Line:
    def __init__(self, c1, c0):
        self.c0 = c0
        self.c1 = c1

    def __call__(self, x):
        return self.c0 + self.c1*x

class Parabola(Line):
    def __init__(self, c0, c1, c2):
        Line.__init__(self, c0, c1)
        self.c2 = c2

    def __call__(self, x):
        return Line.__call__(self, x) + self.c2*x**2

class SinPlusQuadratic(Parabola):                     # SubSubClass
    def __init__(self, A, w, a, b, c):
        Parabola.__init__(self, c, b, a)
        self.A = A
        self.w = w

    def __call__(self, x):
        return Parabola.__call__(self, x) + self.A*sin(self.w*x)

s_q = SinPlusQuadratic(1, pi/2., 1, 1, 1)


# 9.4

class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __str__(self):
        return '(%g, %g)' % (self.x, self.y)


class PolarPoint(Point):
    def __init__(self, r, theta):
        self.r, self.theta = r, theta
        x = r*cos(theta)
        y = r*sin(theta)
        Point.__init__(self, x, y)

    def __str__(self):
        p_string = ' (%g, %g)' % (self.r, self.theta)
        return Point.__str__(self) + p_string

    def __repr__(self):
        return 'PolarPoint(%g, %g)' % (self.r, self.theta)

p2 = PolarPoint(2, pi/4)
print p2
p3 = eval(repr(p2))
print p3
