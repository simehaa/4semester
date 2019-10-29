import matplotlib.pyplot as plt
import numpy as np

# a) position plot

infile = open('pos.dat','r') # file with data
sline = infile.readline()
slist = sline.split()
s = slist[0]                 # obtaining s from the first line
x = []                       # empty lists, because I use append
y = []
for line in infile:
    a = line.split()
    x.append(eval(a[0]))
    y.append(eval(a[1]))
n = len(y)
x = np.asarray(x) # changing x and y to arrays, because I will use different indices in the last loop
y = np.asarray(y)

plt.title('GPS positions')
plt.plot(x,y)
plt.xlabel('time')
plt.ylabel('position')
plt.show()

# b) velocity in x and y direction plot

v_x = np.zeros(n)
v_y = np.zeros(n)

for i in range(n-1):
    v_x[i] = (x[i + 1] - x[i])/float(s)  # simple calculation where I find movement
    v_y[i] = (y[i + 1] - y[i])/float(s)  # each direction and divide by time

plt.plot(x, v_x, label='x direction')    # two plots, for velocity in x and y direction
plt.plot(x, v_y, label='y direction')
plt.title('velocity')
plt.xlabel('time')
plt.ylabel('velocity')
plt.legend()
plt.show()

"""
simen@simen-VirtualBox:~/python/uke8$ python position2velocity.py

"""
