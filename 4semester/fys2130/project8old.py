from math import pi
import numpy as np
import matplotlib.pyplot as plt

def diffEq(xNow,vNow,tNow,mNow):
    """
    differential equation with
    time dependent mass
    """
    return g - ((b + psi)*vNow + k*xNow)/mNow

def RK4(xStart,vStart,tStart,mStart):
    """
    Runge-Kutta method of 4th order,
    with mass updates included.
    A water drop will fall of if
    position exceeds a limit of 0.0025 m
    """
    if xStart > 0.0025:
        dm = abs(beta*mStart*vStart) # water drop mass
        dx = ((C*dm**4)/(mStart**3))**(1./3.)
        mStart -= abs(dm)
        if mStart < 0.00001:
            mStart = 0.00001
        droptimes.append(tStart)
    else:
        dx = 0
    a1 = diffEq(xStart,vStart,tStart,mStart)
    v1 = vStart
    xHalf1 = xStart + v1 * dt/2.0
    vHalf1 = vStart + a1 * dt/2.0
    mHalf1 = mStart + psi*dt/2.0
    a2 = diffEq(xHalf1,vHalf1,tStart+dt/2.0,mHalf1)
    v2 = vHalf1
    xHalf2 = xStart + v2 * dt/2.0
    vHalf2 = vStart + a2 * dt/2.0
    a3 = diffEq(xHalf2,vHalf2,tStart+dt/2.0,mHalf1)
    v3 = vHalf2
    xEnd = xStart + v3 * dt
    vEnd = vStart + a3 * dt
    mEnd = mStart + psi*dt
    a4 = diffEq(xEnd,vEnd,tStart + dt,mEnd)
    v4 = vEnd
    aMiddle = 1.0/6.0 * (a1 + 2*a2 + 2*a3 + a4)
    vMiddle = 1.0/6.0 * (v1 + 2*v2 + 2*v3 + v4)
    xEnd = xStart + vMiddle * dt - dx
    vEnd = vStart + aMiddle * dt
    return xEnd, vEnd, mEnd


if __name__ == '__main__':
    # Global constants
    k = 0.475
    b = 0.001
    g = 9.81
    beta = 50.0
    rho = 1000.
    C = 3./(4*pi*rho)
    # Initial setup
    dt = 0.0001
    T = 20
    n = int(T/dt)
    x = np.zeros(n)
    v = np.zeros(n)
    m = np.zeros(n)
    t = np.linspace(0,T,n)
    m[0] = 0.00001
    x[0] = 0.001
    v[0] = 0.001
    n_p = 3
    psis = np.linspace(0.00055,0.00075,n_p)
    times = np.zeros(n_p)
    # time loop that uses RK4 for each time step
    for j in range(n_p):
        psi = psis[j]
        droptimes = []
        for i in range(n - 1):
            x[i + 1],v[i + 1],m[i + 1] = RK4(x[i],v[i],t[i],m[i])
        for s in range(50):
            diff = np.diff(droptimes[-51:])
            plt.plot(50*[psi*1000],diff,'k.')

    plt.title('drop intervals with different $\psi$')
    plt.xlabel('$\psi \cdot 10^3$ [kg/s]')
    plt.ylabel('time between each of the 50 last drops [s]')
    plt.grid()
    plt.show()

"""
[Command: python -u /home/simen/github/university/4semester/fys2130/project8.py]
[Finished in 208.987s]
"""
