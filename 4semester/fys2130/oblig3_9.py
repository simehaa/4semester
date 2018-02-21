import numpy as np
import matplotlib.pyplot as plt
from math import pi

Fs = 1000
dt = 1./Fs
N = 1024
t = np.linspace(0,(N-1)*dt,N)
for freq in [100,200,400,700,950,1300]:
    x = 0.8*np.cos(2*pi*freq*t)
    X = np.fft.fft(x)*1./N
    frekv = 0.5*Fs*np.linspace(0,1,N*0.5)
    plt.plot(frekv,2*np.abs(X[:int(N*0.5)]),label='%i Hz' % freq)
    plt.title('Absoluttverdier av frekvensspekteret')
    plt.xlabel('Frekvens (Hz)')
    plt.ylabel('|X(frekv)|')
plt.legend()
plt.show()


"""
[Command: python -u /home/simen/github/university/4semester/fys2130/oblig3_9.py]
[Finished in 10.199s]
"""
