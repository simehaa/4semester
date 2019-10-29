# Exercise 2.9: Store values from a formula in lists
g   =  9.81              # (m/s**s) the gravitational acceleration
v0  =  20                # (m/s) velocity
n   =  15                # number of data
dt  =  (2*v0/g)/(n - 1)  # (s) time interval length
t   =  []                # list for time
y   =  []                # list for position

for i in range(0, n):    # appending each equally spaced
    t.append(i*dt)       # time values in the list t
    y.append(v0*t[i] - (1./2)*g*t[i]**2)  # adding the position for each value of t

print '%6s %12s' % ('time:', 'position:') # headline print
for a, b in zip(t, y):                    # zip print with all values
    print '%5.2f s   %-5.2f m' % (a, b)

"""
simen@simen-VirtualBox:~/python/uke2$ python ball_table2.py
 time:    position:
 0.00 s   0.00  m
 0.29 s   5.41  m
 0.58 s   9.99  m
 0.87 s   13.73 m
 1.16 s   16.64 m
 1.46 s   18.72 m
 1.75 s   19.97 m
 2.04 s   20.39 m
 2.33 s   19.97 m
 2.62 s   18.72 m
 2.91 s   16.64 m
 3.20 s   13.73 m
 3.49 s   9.99  m
 3.79 s   5.41  m
 4.08 s   0.00  m
"""
