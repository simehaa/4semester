from math import pi
import numpy as np
import matplotlib.pyplot as plt

class water_drops:
    """Solver of a simulation of a water drop
    using RK4 with mass included. diffEq is the
    differential equation for the system and is given.
    However parameters such as psi, g and b must be
    globally defined, and can be changed"""
    def __init__(self, plot_str='', dt=0.0001, T=20, x0=0.001,  \
                k=0.475, b=0.001, g=9.81, psi=0.00055, rho=1000., \
                xc=0.0025, v0=0.001, beta=50., m0=0.00001):
        self.dt = float(dt)
        self.T = T
        self.n = int(self.T/self.dt)
        self.x = np.zeros(self.n)
        self.v = np.zeros(self.n)
        self.m = np.zeros(self.n)
        self.t = np.linspace(0,self.T,self.n)
        self.x[0] = x0
        self.v[0] = v0
        self.m[0] = m0
        self.m0 = m0
        self.k = k
        self.b = b
        self.g = g
        self.xc = xc
        self.psi = psi
        self.beta = beta
        self.rho = rho
        self.plot_str = plot_str
        self.C = 3./(4*pi*self.rho)
        self.droptimes = []

    def diffEq(self,xNow,vNow,tNow,mNow):
        """ differential equation
        with time dependent mass"""
        return self.g - ((self.b + self.psi)*vNow + self.k*xNow)/mNow

    def solve(self):
        """ method that uses RK4 and diffEq
        to solve the entire motion"""
        for i in range(self.n - 1):
            self.x[i + 1],self.v[i + 1],self.m[i + 1] = self.RK4(self.x[i],self.v[i],self.t[i],self.m[i])

    def RK4(self,xStart,vStart,tStart,mStart):
        """
        Runge-Kutta method of 4th order,
        with mass updates included.
        A water drop will fall of if
        position exceeds a limit of xc
        """
        if xStart > self.xc:
            dm = abs(self.beta*mStart*vStart) # water drop mass
            dx = ((self.C*dm**4)/(mStart**3))**(1./3.)
            mStart -= dm
            if mStart < self.m0:
                mStart = self.m0
            self.droptimes.append(tStart)
        else:
            dx = 0
        a1 = self.diffEq(xStart,vStart,tStart,mStart)
        v1 = vStart
        xHalf1 = xStart + v1 * self.dt/2.0
        vHalf1 = vStart + a1 * self.dt/2.0
        mHalf1 = mStart + self.psi*self.dt/2.0
        a2 = self.diffEq(xHalf1,vHalf1,tStart+self.dt/2.0,mHalf1)
        v2 = vHalf1
        xHalf2 = xStart + v2 * self.dt/2.0
        vHalf2 = vStart + a2 * self.dt/2.0
        a3 = self.diffEq(xHalf2,vHalf2,tStart+self.dt/2.0,mHalf1)
        v3 = vHalf2
        xEnd = xStart + v3 * self.dt
        vEnd = vStart + a3 * self.dt
        mEnd = mStart + self.psi*self.dt
        a4 = self.diffEq(xEnd,vEnd,tStart + self.dt,mEnd)
        v4 = vEnd
        aMiddle = 1.0/6.0 * (a1 + 2*a2 + 2*a3 + a4)
        vMiddle = 1.0/6.0 * (v1 + 2*v2 + 2*v3 + v4)
        xEnd = xStart + vMiddle * self.dt - dx
        vEnd = vStart + aMiddle * self.dt
        return xEnd, vEnd, mEnd

    def plot(self):
        """ plots phase space of motion,
        after solve() method is used"""
        plt.title(self.plot_str)
        plt.plot(self.x,self.v)
        plt.xlabel('position [m]')
        plt.ylabel('velocity [m/s]')
        plt.grid()
        plt.show()


if __name__ == '__main__':
    oppgave7 = water_drops(b=0.0006, k=0.510)
    oppgave7.solve()
    oppgave7.plot()

    diff = np.diff(oppgave7.droptimes)
    n = len(diff)
    drop = np.linspace(1,n,n)
    plt.plot(drop,diff)
    plt.xlabel('drop number')
    plt.ylabel('time between drops [s]')
    plt.grid()
    plt.show()

"""
[Command: python -u /home/simen/github/university/4semester/fys2130/project7.py]
[Finished in 25.923s]
"""
