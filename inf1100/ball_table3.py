g   =  9.81              # (m/s**s) the gravitational acceleration
v0  =  20                # (m/s) velocity
n   =  15                # number of data
dt  =  (2*v0/g)/(n - 1)  # (s) time interval length
time   = []              # list for time
height = []              # list for position

# a)

for i in range(n):       # appending each value equally spaced to t and y
    t = i*dt
    y = v0*t - 1./2*g*t**2
    time.append(t)       # time values in the list t
    height.append(y)     # adding the height for each value of t

ty1 = []                 # empty list
for t, y in zip(time, height):
    ty1.append([t, y])   # filling ty1 with two lists

print ' time    height'
for t, y in ty1:         # the column based print
    print '%5.2f s %5.2f m' % (t, y)

# b)

print '---------------'
print '    time       height'
import pprint
ty2 = []
for t, y in zip(time, height): # the row based print
    t = '%5.2f s' % t
    y = '%5.2f m' % y
    ty2.append([t, y])
pprint.pprint(ty2)

"""
Exercise 2.17 a)
simen@simen-VirtualBox:~/python/uke2$ python ball_table3.py
 time    height
 0.00 s  0.00 m
 0.29 s  5.41 m
 0.58 s  9.99 m
 0.87 s 13.73 m
 1.16 s 16.64 m
 1.46 s 18.72 m
 1.75 s 19.97 m
 2.04 s 20.39 m
 2.33 s 19.97 m
 2.62 s 18.72 m
 2.91 s 16.64 m
 3.20 s 13.73 m
 3.49 s  9.99 m
 3.79 s  5.41 m
 4.08 s  0.00 m
---------------
Exercise 2.17 b)
    time       height
[[' 0.00 s', ' 0.00 m'],
 [' 0.29 s', ' 5.41 m'],
 [' 0.58 s', ' 9.99 m'],
 [' 0.87 s', '13.73 m'],
 [' 1.16 s', '16.64 m'],
 [' 1.46 s', '18.72 m'],
 [' 1.75 s', '19.97 m'],
 [' 2.04 s', '20.39 m'],
 [' 2.33 s', '19.97 m'],
 [' 2.62 s', '18.72 m'],
 [' 2.91 s', '16.64 m'],
 [' 3.20 s', '13.73 m'],
 [' 3.49 s', ' 9.99 m'],
 [' 3.79 s', ' 5.41 m'],
 [' 4.08 s', ' 0.00 m']]
"""
