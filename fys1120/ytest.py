import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
a = np.zeros(1)
a[0] = 2.
print a**0
"""
T = 1e-6
dt = 1e-9
n = int(T/dt)
q_e = - 1.6e-19
m_e = 9.11e-31
a = np.zeros(3)
a[0] = 1
a[1] = 2
a[2] = -5
a *= q_e/m_e*-1
r = np.zeros((n,3))
v = np.zeros((n,3))
t = np.linspace(0,T,n)
for i in range(n - 1):
    v[i + 1] = v[i] + a*dt
    r[i + 1] = r[i,:] + v[i + 1]*dt

plt.plot(t,r[:,0],label='x(t)')
plt.plot(t,r[:,1],label='y(t)')
plt.plot(t,r[:,2],label='z(t)')
plt.xlabel('t [s]')
plt.ylabel('position [m]')
plt.legend()
plt.show()

fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')
ax.plot(r[:,0],r[:,1],r[:,2])
plt.xlabel('x [m]'); plt.ylabel('y [m]'); ax.set_zlabel('z [m]')
plt.show()"""
