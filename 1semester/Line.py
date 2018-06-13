# 7.6
class Line:
    def __init__(self, p1, p2):
        self.x0 = p1[0] # obtaining x and y coordinates from list/tuple
        self.y0 = p1[1]
        self.x1 = p2[0]
        self.y1 = p2[1]

    def value(self, x):
        a = (self.y1 - self.y0)/float(self.x1 - self.x0) # slope of the line
        b = self.y0 - a*self.x0                          # constant terms (f(0))
        return (a*x + b)

def test_Line():
    # line: 1.5*x - 3
    p1 = [-1, -4.5]
    p2 = [3, 1.5]
    line = Line(p1,p2)
    # value at x=1, should be -1.5
    expected = -1.5
    computed = line.value(1)
    tol = 1e-14
    success = abs(expected - computed) < tol
    msg = 'failed! expected %.f got %.f' % (expected, computed)
    assert success, msg

"""
simen@simen-VirtualBox:~/python/uke9$ python
Python 2.7.12 (default, Jul  1 2016, 15:12:24)
[GCC 5.4.0 20160609] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> from Line import Line, test_Line
>>> line = Line((0,-1), (2,4))
>>> print line.value(0.5), line.value(0), line.value(1)
0.25 -1.0 1.5
>>> test_Line()
>>>
"""
