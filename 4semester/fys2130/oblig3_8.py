import numpy as np
import matplotlib.pyplot as plt
from math import pi

np.random.seed(100)
Fs = 1000
dt = 1./Fs
N = 1024
t = np.linspace(0,(N-1)*dt,N)
freq = 200
x = 0.8*np.cos(2*pi*freq*t) + np.random.normal(0,0.2,N)
X = np.fft.fft(x)*1./N
print "average signal  = %f" % np.mean(x)
print "first point fft = %f" % np.real(X[0])

"""
[Command: python -u /home/simen/github/university/4semester/fys2130/oblig3_8.py]
average signal  = -0.002900
first point fft = -0.002900
[Finished in 2.161s]
"""
