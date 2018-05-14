import numpy as np
import matplotlib.pyplot as plt

diameter = np.array([10.3,9.6,10.0,10.0,10.0,9.9,10.0,10.0,10.0]) # 9 maalinger jevnt fordelt
radius = 0.5*np.mean(diameter)
dr     = np.sqrt((0.5*np.std( diameter))**2 + (0.1/2)**2)

A = np.pi*radius**2*1e-6 # mm**2 
dA = A*np.sqrt(2)*np.sqrt((0.08/radius)**2 + (0.01/radius)**2)
#print(A, '+/-', dA)
u0 = 4*np.pi*1e-7

Fz =   -1*np.array([0,0.02,0.03,0.05,0.07,0.1,0.16,0.18,0.21,0.24,0.27,0.3,0.34])*0.001*9.81 # N
dFz =   np.array([0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01])*0.001*9.81 #np.abs(0.005*Fz)
B1 =    np.array([19,110,210,302,388,464,537,600,655,700,740,770,805])*0.001 # T
dB1 =   np.array([0.3,2,1,2,5,2,5,5,10,5,10,10,15])*0.001
B2 =    np.array([0.3,0.7,1.5,2.2,3.2,2.9,3.3,2.5,3.1,3.0,2.8,2.7,2.9])*0.001
dB2 =   np.array([0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1])*0.001

Btot = (B1**2 - B2**2)
x = (1/(2*u0))*A*Btot
dBtot = 2*np.sqrt(dB1**2 + dB2**2)
dx = np.sqrt((dBtot/Btot)**2 + (dA/A)**2)*x

plt.errorbar(x,Fz,xerr=dx,yerr=dFz,fmt='bo',label='datapunkter med usikkerhet')
plt.ylabel(r'$F_z$,  [N]')
plt.xlabel(r'$(B_1^2 - B_2^2)A/2\mu_0$,  $[N^{-1}]$')
plt.grid()

def lin(x,y,deg):
    p = np.polyfit(x,y,deg)
    yline = np.polyval(p,x)
    n = len(x)
    m = p[0]
    c = p[1]
    D = np.sum(x*x) - (np.sum(x))**2/n
    E = np.sum(x*y) - np.sum(x)*np.sum(y)/n
    F = np.sum(y*y) - (np.sum(y))**2/n
    dm = np.sqrt((1/(n - 2))*(D*F - E**2)/D**2)
    dc = np.sqrt((1/(n - 2))*(D/n + (np.mean(x))**2)*((D*F - E**2)/D**2))

    yline = np.polyval(p,x)
    plt.title('linjetilpasning $F_z = \chi (B_1^2 - B_2^2)A/2\mu_0, \chi = %1.6f \pm %1.6f$' % (m,dm))
    plt.plot(x,yline,label='linjetilpasning')
    plt.legend()
    plt.show()
    return m,dm,c,dc

m,dm,c,dc = lin(x,Fz,1)