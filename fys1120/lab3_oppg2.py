import numpy as np
import matplotlib.pyplot as plt

u0 = np.pi*4e-7
Js = 1
t = 35e-3
a = 20e-3

def Bx(h):
    return u0/2.*Js*((h + t)/np.sqrt((h + t)**2 + a**2) - h/np.sqrt(h**2 + a**2))

h = np.linspace(0.4,2,100)
plt.plot(h,Bx(h))
plt.show()
