# 7.4
from math import sqrt

class Rectangle:
    def __init__(self, w, h, lower_left): # don't actually need lower left corner for area and perimeter
        self.w = w                        # I could've used two points, and found width with x1 - x0 and heigth with y1 - y0
        self.h = h
        self.lower_left = lower_left

    def area(self):
        return self.w*self.h # the area: side * other_side

    def perimeter(self):
        return 2*(self.w + self.h) # the perimeter both sides added * 2

class Triangle:
    def __init__(self, vertices): # vertices is a nested list/tuple
        self.x0, self.x1, self.x2 = vertices[0][0], vertices[1][0], vertices[2][0]
        self.y0, self.y1, self.y2 = vertices[0][1], vertices[1][1], vertices[2][1]

    def area(self): # function for area
        return abs(self.x0*(self.y1 - self.y2) + self.x1*(self.y2 - self.y0) + self.x2*(self.y0 - self.y1))/2.

    def perimeter(self): # function for side length, using pytagoras on each side, then adding the lengths together
        len0 = sqrt((self.x1 - self.x0)**2 + (self.y1 - self.y0)**2)
        len1 = sqrt((self.x2 - self.x0)**2 + (self.y2 - self.y0)**2)
        len2 = sqrt((self.x2 - self.x1)**2 + (self.y2 - self.y1)**2)
        return len0 + len1 + len2


def test_Rectangle():
    # sides: 5 and 6
    exp_area = 30.  # 5*6
    exp_peri = 22.  # 5 + 5 + 6 + 6
    r = Rectangle(5, 6, (0,0))  # calling class Rectangle to object r
    com_area = r.area()
    com_peri = r.perimeter()
    tol = 1e-14
    success = abs(exp_area - com_area) < tol and abs(exp_peri - com_peri) < tol
    msg = 'class failed! Area - expected %.2f got %.2f, Perimeter - expected %.2f got %.2f' % (exp_area, com_area, exp_peri, com_peri)
    assert success, msg

test_Rectangle()

def test_Triangle():
    # coordinates (0,0), (4,0) and (0,3)
    exp_area = 6.  # (4*3)/2.
    exp_peri = 12. # 3 + 4 + 5
    vertices = ((0,0),(4,0),(0,3))
    t = Triangle(vertices)
    com_area = t.area()
    com_peri = t.perimeter()
    tol = 1e-14
    success = abs(exp_area - com_area) < tol and abs(exp_peri - com_peri) < tol
    msg = 'class failed! Area - expected %.2f got %.2f, Perimeter - expected %.2f got %.2f' % (exp_area, com_area, exp_peri, com_peri)
    assert success, msg

test_Triangle()

"""
simen@simen-VirtualBox:~/python/uke9$ python geometric_shapes.py
"""
