import numpy as np
import matplotlib.pyplot as plt
from math import atan
import numpy.polynomial.polynomial as poly

## Refraction value for air ##
na = 1.00 # assumption for air


def readfiles(filename):
    angles = []
    intensity = []
    infile = open(filename, 'r')
    for line in infile:
        a = line.split()
        b = a[0].replace(',','.')
        c = a[1].replace(',','.')
        angles.append(eval(b))
        intensity.append(eval(c))
    infile.close()
    theta = 90 - np.asarray(angles)
    inten = np.asarray(intensity)*0.01
    return(theta,inten)
 
    
# readfiles
t1,i1 = readfiles('run1.txt')
t2,i2 = readfiles('run2.txt')
t3,i3 = readfiles('run3.txt')


# gotta find that angle on the bottom of the curve
def n(t,I):
    i = np.argmin(I)
    bottomangle = (t[i])*np.pi/180
    n = na*np.tan(bottomangle)
    return n

n1 = n(t1,i1)
n2 = n(t2,i2)

def plotrs(n2):
    A = np.linspace(0,90,1001)*np.pi/180
    Rs = ((na*np.cos(A) - n2*np.sqrt(1 - (na*np.sin(A)/n2)**2)) / (na*np.cos(A) + n2*np.sqrt(1 - (na*np.sin(A)/n2)**2)))**2
    plt.plot(A*180/np.pi,Rs,'b-',label='$R_s$ for n = %1.2f' % n2)

def plotrp(n2):
    A = np.linspace(0,90,1001)*np.pi/180
    Rp = ((n2*np.cos(A) - na*np.sqrt(1 - (na*np.sin(A)/n2)**2)) / (n2*np.cos(A) + na*np.sqrt(1 - (na*np.sin(A)/n2)**2)))**2
    plt.plot(A*180/np.pi,Rp,'r-',label='$R_p$ for n = %1.2f' % n2)
    
#plot_Rs_Rp(1.5)
## RUN 1, p-polarisert, 1 gain ##

mid = np.argmin(i1)
i1_left = i1[mid:]
i1_right = i1[:mid]
il = np.argmin(np.abs(t1-48))
ir = np.argmin(np.abs(t1-60))
#plt.plot(t2[:mid],i2[:mid],'ro')
#plt.plot(t2[mid:],i2[mid:],'go')

def lin(x,y,deg=2):
    p = np.polyfit(x,y,deg)
    x_new = np.linspace(np.min(x),np.max(x),1001)
    yline = np.polyval(p,x_new)
    a = p[0]
    b = p[1]
    xmid = -b/(2*a)
    print(xmid)
    dtheta = np.sqrt(2**2 + 3**2)
    plt.plot(x_new,yline,'y.',label='Kurvetilpasning')
    plt.plot([xmid,xmid],[0,1],'k--',label=r'$\theta_B = (%2.0f \pm %2.0f)^\circ$' % (xmid,dtheta))
    return np.tan(xmid*np.pi/180)
plt.plot(t1,i1,'k.',label='Målepunkter, Kjøring 1')
n = lin(t1[ir:il],i1[ir:il])
plt.title(r'Kjøring 1, p-polarisert, 1 gain, $n_{glass} = %1.2f \pm %1.2f$' % (n,0.21))
plotrp(n)
n1 = n
plt.grid()
plt.axis([0,90,0,1])
plt.xlabel(r'Innfallsvinkel $\theta_i [^\circ]$')
plt.ylabel('Lysintensitet [relativ]')
plt.legend(loc='best')
plt.show()

## RUN 2, p-polarisert, 10 gain ##
mid = np.argmin(i2)
i2_left = i2[mid:]
i2_right = i2[:mid]
il = np.argmin(np.abs(t2-48))
ir = np.argmin(np.abs(t2-60))
#plt.plot(t2[:mid],i2[:mid],'ro')
#plt.plot(t2[mid:],i2[mid:],'go')

def lin(x,y,deg=2):
    p = np.polyfit(x,y,deg)
    x_new = np.linspace(np.min(x),np.max(x),1001)
    yline = np.polyval(p,x_new)
    a = p[0]
    b = p[1]
    xmid = -b/(2*a)
    dtheta = np.sqrt(2**2 + 1**2)
    plt.plot(x_new,yline,'y.',label='Kurvetilpasning')
    plt.plot([xmid,xmid],[0,1],'k--',label=r'$\theta_B = (%2.1f \pm %2.1f)^\circ$' % (xmid,dtheta))
    return np.tan(xmid*np.pi/180)
plt.plot(t2,i2,'k.',label='Målepunkter, Kjøring 2')
n = lin(t2[ir:il],i2[ir:il])
plt.title(r'Kjøring 2, p-polarisert, 10 gain, $n_{glass} = %1.2f \pm %1.2f$' % (n,0.12))
plotrp(n)
B = t2[np.argmin(i2)]
n2 = n
#plt.plot([B,B],[0,1],'k--',label=r'Brewstervinkel, $\theta_B = %2.1f^\circ$' % B)
plt.grid()
plt.axis([0,90,0,1])
plt.xlabel(r'Innfallsvinkel $\theta_i [^\circ]$')
plt.ylabel('Lysintensitet [relativ]')
plt.legend(loc=3)
plt.show()

## RUN 3, s-polarisert, 10 gain: forventer jevn økning ##
n_final = n2
plt.title(r'Kjøring 3, s-polarisert, 10 gain')
plotrs(n_final)
plt.plot(t3,i3,'k.',label='Kjøring 3')
plt.grid()
plt.axis([0,90,0,1])
plt.xlabel(r'Innfallsvinkel $\theta_i [^\circ]$')
plt.ylabel('Lysintensitet [relativ]')
plt.legend(loc='best')
plt.show()