import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def euler_cromer_oppg2(pos,vel,T,dt,n):
    B = np.zeros(3)
    B[2] = 2.0        # constant magnetic field in z direction
    q_e = - 1.6e-19
    m_e = 9.11e-31

    def a(v):
        return (q_e/m_e)*(np.cross(v,B))

    r = np.zeros((n,3))
    v = np.zeros((n,3))
    t = np.linspace(0,T,n)
    r[0,:] = pos # initial
    v[0,:] = vel # initial

    for i in range(n - 1):
        v[i + 1] = v[i] + a(v[i])*dt
        r[i + 1] = r[i,:] + v[i + 1]*dt

    return r,v,t


def plot_oppg2(pos,vel,T,dt,n,period=False,plotpos=False,plotvel=False,plot3d=False):
    r,v,t = euler_cromer_oppg2(pos,vel,T,dt,n)

    if period:
        tol = 2
        a = []
        for i in range(n):
            if abs(v[i,0] - v[i,1]) < tol:
                a.append(t[i])
        print "period = %e s" % (a[2] - a[0])

    if plotpos:
        plt.plot(t,r[:,0],label='x(t)')
        plt.plot(t,r[:,1],label='y(t)')
        plt.plot(t,r[:,2],label='z(t)')
        plt.xlabel('t [s]')
        plt.ylabel('position [m]')
        plt.legend()
        plt.grid(True)
        plt.show()

    if plotvel:
        plt.plot(t,v[:,0],label='vx(t)')
        plt.plot(t,v[:,1],label='vy(t)')
        plt.plot(t,v[:,2],label='vz(t)')
        plt.xlabel('t [s]')
        plt.ylabel('velocity [m/s]')
        plt.legend()
        plt.grid(True)
        plt.show()

    if plot3d:
        fig = plt.figure()
        ax = fig.add_subplot(111,projection='3d')
        ax.plot(r[:,0],r[:,1],r[:,2])
        plt.xlabel('x [m]'); plt.ylabel('y [m]'); ax.set_zlabel('z [m]')
        plt.show()


pos = np.zeros(3)
vel = np.zeros(3)
vel[0] = 10000.
T = 30e-12
dt = 1e-15
n = int(T/dt)
# plot_oppg2(pos,vel,T,dt,n,period=True,plotpos=True,plotvel=True,plot3d=True)
vel[0] = 5000.
vel[2] = 2000.
# plot_oppg2(pos,vel,T,dt,n,plot3d=True)


def euler_cromer_oppg3(pos,vel,T,dt,n,b,d,Rd):
    m_p = 1.67e-27
    q_p = 1.6e-19
    E0 = np.zeros(3); E0[0] = 25000./d
    B = np.zeros(3); B[2] = b

    def a(v,r,t):
        if np.sqrt(r[0]**2 + r[1]**2) > Rd: # check if particle is inside the cyclotron
            return 0
        else:
            if abs(r[0]) < d/2: # results in E field
                k = np.cos(q_p*b*t/m_p)
            else: # when particle is outside the valley gap, there is no E field
                k = 0
            return (q_p/m_p)*(np.cross(v,B) + k*E0) # total acceleration

    r = np.zeros((n,3))
    v = np.zeros((n,3))
    t = np.linspace(0,T,n)
    r[0,:] = pos
    v[0,:] = vel
    for i in range(n - 1):
        v[i + 1] = v[i] + a(v[i],r[i],t[i])*dt
        r[i + 1] = r[i,:] + v[i + 1]*dt

    return r,v,t


def plot_oppg3(pos,vel,T,dt,n,B,d,Rd,plotxy=False,plotpos=False,plotvel=False,esc_vel=False):
    r,v,t = euler_cromer_oppg3(pos,vel,T,dt,n,B,d,Rd)

    if plotxy:
        plt.plot(r[:,0],r[:,1],label='posisjon i xy-planet')
        plt.xlabel('x [m]')
        plt.ylabel('y [m]')
        plt.legend()
        plt.grid(True)
        plt.show()

    if esc_vel:
        ve = np.sqrt(v[n-1,0]**2 + v[n-1,1]**2 + v[n-1,2]**2)
        print "escape velocity = %.2f m/s = %.2f c" % (ve, ve/299792458)

    if plotpos:
        plt.plot(t,r[:,0],label='x(t)')
        plt.plot(t,r[:,1],label='y(t)')
        plt.plot(t,r[:,2],label='z(t)')
        plt.xlabel('t [s]')
        plt.ylabel('position [m]')
        plt.legend()
        plt.grid(True)
        plt.show()

    if plotvel:
        plt.plot(t,v[:,0],label='vx(t)')
        plt.plot(t,v[:,1],label='vy(t)')
        plt.plot(t,v[:,2],label='vz(t)')
        plt.xlabel('t [s]')
        plt.ylabel('velocity [m/s]')
        plt.legend()
        plt.grid(True)
        plt.show()


pos = np.zeros(3)
vel = np.zeros(3)
T = 300e-9
dt = 100e-15
n = int(T/dt)
B = 1.9
d = 90e-6
Rd = 100
# plot_oppg3(pos,vel,T,dt,n,B,d,Rd,plotxy=True)
Rd = 50e-3
# plot_oppg3(pos,vel,T,dt,n,B,d,Rd,plotpos=True,plotvel=True,esc_vel=True)

"""
period = 1.788819e-11 s
escape velocity = 8332266.31 m/s = 0.03 c
"""
