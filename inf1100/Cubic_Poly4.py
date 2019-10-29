class Line:
    def __init__(self, c0, c1):
        self.c0 = c0
        self.c1 = c1

    def __call__(self, x):
        print 'Line called'
        return self.c0 + self.c1*x # line c1*x + c0

    def table(self, L, R, n): # this function takes self, and will work for Parabola, Cubic and Poly4
        s = '' # empty string
        import numpy as np
        for x in np.linspace(L, R, n): # easiest way to deal with non-integer steplengths
            s += '%.2f %.2f\n' % (x, self(x)) # adding new line to string
        return s


class Parabola(Line):
    def __init__(self, c0, c1, c2):
        Line.__init__(self, c0, c1)
        self.c2 = c2

    def __call__(self, x):
        print 'Parabola called'
        return Line.__call__(self, x) + self.c2*x**2 # Parabola c2*x**2 + line from Line


class Cubic(Parabola):
    def __init__(self, c0, c1, c2, c3):
        Parabola.__init__(self, c0, c1, c2)
        self.c3 = c3

    def __call__(self, x):
        print 'Cubic called'
        return Parabola.__call__(self, x) + self.c3*x**3 # Cubic c3*x**3 + parabola from Parabola


class Poly4(Cubic):
    def __init__(self, c0, c1, c2, c3, c4):
        Cubic.__init__(self, c0, c1, c2, c3)
        self.c4 = c4

    def __call__(self, x):
        print 'Poly4 called'
        return Cubic.__call__(self, x) + self.c4*x**4 # 4th degree polynomial: c4*x**4 + Cubic polynomial


cu = Cubic(3, 5, -1, 2)
print cu(2)
p4 = Poly4(2, 4, 1, -1, 1)
print p4(1)

"""
simen@simen-VirtualBox:~/python/uke10$ python Cubic_Poly4.py
Cubic called
Parabola called
Line called
25
Poly4 called
Cubic called
Parabola called
Line called
7
"""
