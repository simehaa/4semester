from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
from math import pi

infile = open('soldata.dat','r')
x,y = [],[]
for line in infile:
    a = line.split()
    x.append(eval(a[0]))
    y.append(eval(a[1]))
infile.close()
times = np.array(x)
sunspots = np.array(y)

N = float(len(times))
dt = times[1]-times[0]
X = np.fft.fft(sunspots)
f = np.fft.fftfreq(len(sunspots),dt)
f1 = f[1:int(N/2)]
X1 = np.abs(X*2/N)[1:int(N/2)]
i = X1.argmax()
fmax = f[i]

plt.figure()
plt.subplot(211)
plt.plot(times,sunspots)
plt.ticklabel_format(useOffset=False)
plt.grid(True)
plt.title("Sunspots, peak frequency = %f Hz" % fmax)
plt.xlabel("time [year]")
plt.ylabel("Number of sunspots")
plt.subplot(212)
plt.plot(f1,X1)
plt.xlabel("frequency [Hz]")
plt.ylabel("Amplitude")
plt.ticklabel_format(useOffset=False)
plt.grid(True)
plt.show()

"""
simen@simenlinux:~/github/university/4semester/fys2130$

"""
