import numpy as np
import matplotlib.pyplot as plt
from math import atan
from mpl_toolkits.mplot3d import Axes3D

na = 1.00027715
n2 = 1.5150
A = np.linspace(0,np.pi/2,1001)
Rs = ((na*np.cos(A) - n2*np.sqrt(1 - (na*np.sin(A)/n2)**2)) / (na*np.cos(A) + n2*np.sqrt(1 - (na*np.sin(A)/n2)**2)))**2
Ts = 1 - Rs
Rp = ((n2*np.cos(A) - na*np.sqrt(1 - (na*np.sin(A)/n2)**2)) / (n2*np.cos(A) + na*np.sqrt(1 - (na*np.sin(A)/n2)**2)))**2
Tp = 1 - Rp


B = atan(n2/na)*180/np.pi
plt.title(r'$n_1 = %1.5f$, $n_2 = %1.4f$, $\theta_B = %1.2f^\circ$' % (na,n2,B))
plt.plot(A*180/np.pi,Rs,'b-',label='$R_s$')
plt.plot(A*180/np.pi,Rp,'r-',label='$R_p$')
plt.plot(A*180/np.pi,1-Rs,'b--',label='$T_s$')
plt.plot(A*180/np.pi,1-Rp,'r--',label='$T_p$')
plt.plot([B,B],[0,1], 'k--', label='Brewstervinkelen')
plt.legend()
plt.grid()
plt.axis([0,90,-0.01,1.01])
plt.xlabel(r'$\theta_i$ [$^\circ$]')
plt.ylabel('Relativ lysintensitet')



l = 550e-9
no = 1.6583
ne = 1.4864


t = (l/(4*(no-ne)))


no = 1.6613
ne = 1.4875
phase = 2*np.pi*t*(no-ne)/(590e-9)
phase*=2
n = 1001
t = np.linspace(0,4*np.pi,n)
r1 = np.zeros((n,3))
r1[:,0] = t
r1[:,1] = np.cos(t)

r2 = np.zeros((n,3))
r2[:,0] = t
r2[:,2] = np.cos(t+phase)

r3 = np.zeros((n,3))
r3[:,0] = t
r3[:,1] = r1[:,1]
r3[:,2] = r2[:,2]

fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')
ax.plot(r1[:,0],r1[:,1],r1[:,2],'b--')
ax.plot(r2[:,0],r2[:,1],r2[:,2],'g--')
ax.plot(r3[:,0],r3[:,1],r3[:,2],'r-')
#plt.xlabel('x [m]'); plt.ylabel('y [m]'); ax.set_zlabel('z [m]')
plt.show()








