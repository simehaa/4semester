import numpy as np
import matplotlib.pyplot as plt

x0 = 5. # fm
a = 1. # fm
k = 1.38 # fm**-1
A = (2*np.pi*a**2)**(-1./4.)

x = np.linspace(-2.5,12.5,1001)
Psi = A*np.exp(-(x - x0)**2/(4*a**2))*np.exp(1j*k*x)

plt.plot(x,np.absolute(Psi))
plt.xlabel("distance [fm]")
plt.ylabel("|Psi(x,0)|**2")
plt.grid()
plt.show()
