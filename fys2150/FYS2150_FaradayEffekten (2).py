import numpy as np
import matplotlib.pyplot as plt
from Usikkerhetsklasse_gabrielcabrera import uFloat as uF
from Usikkerhetsklasse_gabrielcabrera import uArray as uA
from Usikkerhetsklasse_gabrielcabrera import list_to_uArray as luA
import Usikkerhetsklasse_gabrielcabrera as UK


theta440_arr=np.array((5.0, 3.4, 2.8, 1.8, 1.2, 0.6, 0.0, 0.0, -0.4, -1.6, -2.4, -3.0, -4.2, -5.2))*np.pi/180. #rad
theta580_arr=np.array((4.8, 4.2, 3.4, 2.6, 1.6, 0.8, 0.0, 0.0, -0.8, -2.0, -2.8, -3.6, -4.2, -5.0))*np.pi/180.
theta595_arr=np.array((4.4, 3.6, 2.8, 2.2, 1.6, 0.8, 0.0, 0.0, -0.6, -1.4, -2.4, -3.0, -3.8, -4.4))*np.pi/180.
I440_arr=np.array((3.00, 2.51, 1.99, 1.46, 1.01, 0.51, 0.00, 0.00, -0.47, -1.01, -1.54, -2.03, -2.56, -3.03)) #ampere
I580_arr=np.array((2.99, 2.51, 2.04, 1.48, 1.01, 0.44, 0.00, 0.00, -0.47, -1.07, -1.53, -2.04, -2.51, -3.04))
I595_arr = np.array((3.02, 2.55, 2.02, 1.54, 1.00, 0.54, 0.00, 0.00, -0.45, -1.01, -1.52, -2.01, -2.54, -3.00))

I440 = np.ndarray.tolist(I440_arr)
I580 = np.ndarray.tolist(I580_arr) 
I595 = np.ndarray.tolist(I595_arr)
dtheta = 0.2*np.pi/180.
dI440_arr = np.sqrt((0.015*I440_arr)**2 + 0.02**2)
dI580_arr = np.sqrt((0.015*I580_arr)**2 + 0.02**2)
dI595_arr = np.sqrt((0.015*I595_arr)**2 + 0.02**2)

dI440 = np.ndarray.tolist(dI440_arr)
dI580 = np.ndarray.tolist(dI580_arr) 
dI595 = np.ndarray.tolist(dI595_arr)





# linjetilpasning B
def lin(x,y,deg=1):
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
    plt.title(r'$B(I) = (%1.4f \pm %1.4f)I + (%1.4f \pm %1.4f)$' % (m,dm,c,dc))
    plt.plot(x,yline,'b-',label='Linear regression')
    plt.plot(x,y,'bo',label='Specified $B_{max}(I)$')
    plt.grid()
    plt.legend()
    plt.xlabel('I [A]')
    plt.ylabel('B [T]')
    plt.show()
    return m,dm,c,dc,yline


I = np.array([1.0,1.5,2.0,2.5,3.0])
B = np.array([43,63,83,102,119])*1e-3
m,dm,c,dc,yline = lin(I,B,1)
L = 0.03
f = 1.5
df = 0.1
dL = 0.001

def LB(m,dm,c,dc,f,df,I,dI,L,dL):
    LB_ = (m*I + c)*L/f
    d1 = np.sqrt((dm/m)**2 + (dI/I)**2)*m*I # Tesla
    d2 = np.sqrt(d1**2 + dc**2) # Tesla
    d3 = np.sqrt((d2/(m*I + c))**2 + (dL/L)**2 +(df/f)**2)*LB_
    return LB_, d3




LB440_arr,dLB440 = LB(m,dm,c,dc,f,df,I440_arr,dI440_arr,L,dL)
LB580_arr,dLB580 = LB(m,dm,c,dc,f,df,I580_arr,dI580_arr,L,dL)
LB595_arr,dLB595 = LB(m,dm,c,dc,f,df,I595_arr,dI595_arr,L,dL)


# plots av theta vs LB
def linplot(x,y,xerr,yerr,i):
    deg = 1
    p = np.polyfit(x,y,deg)
    yline = np.polyval(p,x)
    n = float(len(x))
    m = p[0]
    c = p[1]
    D = np.sum(x*x) - (np.sum(x))**2/n
    E = np.sum(x*y) - np.sum(x)*np.sum(y)/n
    F = np.sum(y*y) - (np.sum(y))**2/n
    dm = np.sqrt((1/(n - 2))*(D*F - E**2)/D**2)
    dc = np.sqrt((1/(n - 2))*(D/n + (np.mean(x))**2)*((D*F - E**2)/D**2))
    yline = np.polyval(p,x)

    plt.title('$\lambda = %i nm$, V = %1.4g $\pm$ %1.2g [$rad \cdot m^{-1}T^{-1}$]' % (i,m,dm))
    plt.errorbar(x,y,xerr=xerr,yerr=yerr,fmt='bo',label='datapunkter')
    plt.plot(x,yline,label='linjetilpasning')
    plt.xlabel(r'$LB [T\cdot m]$')
    plt.ylabel(r'$\theta [rad]$')
    plt.grid()
    plt.legend()
    plt.show()

    return m,dm


m440,dm440 = linplot(LB440_arr,theta440_arr,dLB440,dtheta,440)
m580,dm580 = linplot(LB580_arr,theta580_arr,dLB580,dtheta,580)
m595,dm595 = linplot(LB595_arr,theta595_arr,dLB595,dtheta,595)
print(dm440,dm580,dm595)
"""
l = [440,580,595]
V = [m440,m580,m595]
plt.plot(l,V,'ro')
plt.xlabel(r'$\lambda [nm]$')
plt.ylabel('Verdet constant')
plt.grid()
plt.show()"""
