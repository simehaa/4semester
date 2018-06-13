from math import sin, asinh, pi

n = 2*pi
d = float(raw_input("How many values? "))
v = n/d
angle = 0

print 'angle      asinh'
while angle <= n:
    value_asinh = asinh(angle)
    angle += v
    print '%5.2f %5.2f' % (angle, value_asinh)
