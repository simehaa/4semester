import scipy.io
import numpy as np
import matplotlib.pyplot as plt
import pylab
import numpy.polynomial.polynomial as poly

a = scipy.io.loadmat('RC_data.mat')
f = a["frekvens"]; f = np.asarray(f)
v = a["Vu_over_Vi"]; v = np.asarray(v)
plt.plot(f,v,'ko')
plt.yscale('log')
plt.xscale('log')

f9 = f[0,-9:]
v9 = v[0,-9:]
f0 = f[0,0]
f1 = f[0,-1]
t = np.linspace(f0,f1,1000)
p = np.polyfit(f9,v9,0)
print p
plt.plot
# w0 = 10**p[-1]
p = 10**p
y = np.polyval(p,t)
# print w0
# y = (1 + (f/w0)**2)**(-0.5)
plt.plot(t,y,'ro')

plt.show()
