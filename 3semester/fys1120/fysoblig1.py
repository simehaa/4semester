import numpy as np
import matplotlib.pyplot as plt

v0 = 10
rho = - 1e-5
d = 0.01
e0 = 8.85e-12

x = np.linspace(0,d,101)
V = -(rho*x**2/(2*e0)) + ((rho*d/(2*e0)) - (v0/d))*x + v0
plt.plot((d,d),(-v0,v0),'r--'); plt.plot((0,0),(-v0,v0),'r--'); plt.plot((0,d),(0,0),'k--')
plt.xlabel('x [m]')
plt.ylabel('V(x) [volt]')
plt.plot(x,V, label='Potensialet V')
plt.grid(True)
plt.legend()
plt.show()

E = (rho/e0)*x + v0/d - rho*d/(2*e0)
plt.plot((d,d),(-v0,v0),'r--'); plt.plot((0,0),(-v0,v0),'r--'); plt.plot((0,d),(0,0),'k--')
plt.xlabel('x [m]')
plt.ylabel('Ex(x) [F/q]')
plt.plot(x,E, label='x-komponenten til elektriske feltet')
plt.grid(True)
plt.legend()
plt.show()
