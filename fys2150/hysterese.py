import numpy as np
import matplotlib.pyplot as plt

# kjoring 1-12 \ nr 3
Imax = np.array([ 4.41, 3.93, 3.44, 2.96, 2.53, 2.13, 1.72, 1.31, 0.90, 0.55])
Imin = np.array([-4.61,-4.06,-3.58,-3.10,-2.69,-2.27,-1.86,-1.45,-1.03,-0.69])

I = np.abs(Imax - Imin)/2

Smax = np.array([ 459.47, 1109.96, 1053.18, 857.0,    0.00, 459.47,  495.61, 10.33,      5.16,  15.49])
Smin = np.array([-712.44, -15.49,  -5.16, -108.42, -841.51, -237.48, -15.49, -249.27, -139.39, -56.79])

deltaS = np.abs(Smax - Smin)

k = 1.01e-6
n = 130
r = 6.5e-3/2
A = np.pi*r**2
mu0 = 4*np.pi*1e-7
N = 344
L = 0.315
B = k*deltaS/(n*A)
H0 = I*N/L
M = deltaS*k/(2*n*A*mu0) - H0
plt.plot(I,B,'bo',I,B,'b-')
plt.xlabel('I [A]')
plt.ylabel('B [T]')
plt.grid()
plt.show()

plt.plot(H0,M,'bo',H0,M,'b-')
#Iarray = np.linspace(0,5,100)
#t = 1/0.4
#R = 0.5
#dS = R/k * Iarray* ( np.sin(0.8*np.pi*t/2.*I))
#H0 = Iarray*N/L
#M = dS*k/(2*n*A*mu0) - H0
#plt.plot(H0,M)
#p = np.polyfit(H0,M,5)
#H0new = np.linspace(np.min(H0),np.max(H0),100)
#Mnew = np.polyval(p,H0new)
#plt.plot(H0new,Mnew)
plt.xlabel('$H_0$ [A/m]')
plt.ylabel('M [A/m]')
plt.grid()
plt.show()


