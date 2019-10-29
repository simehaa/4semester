import numpy as np
import matplotlib.pyplot as plt

theta440_arr=np.array((5.0, 3.4, 2.8, 1.8, 1.2, 0.6, 0.0, 0.0, -0.4, -1.6, -2.4, -3.0, -4.2, -5.2))*180/np.pi #rad
theta580_arr=np.array((4.8, 4.2, 3.4, 2.6, 1.6, 0.8, 0.0, 0.0, -0.8, -2.0, -2.8, -3.6, -4.2, -5.0))*180/np.pi
theta595_arr=np.array((4.4, 3.6, 2.8, 2.2, 1.6, 0.8, 0.0, 0.0, -0.6, -1.4, -2.4, -3.0, -3.8, -4.4))*180/np.pi
I440_arr=np.array((3.00, 2.51, 1.99, 1.46, 1.01, 0.51, 0.00, 0.00, -0.47, -1.01, -1.54, -2.03, -2.56, -3.03)) #ampere
I580_arr=np.array((2.99, 2.51, 2.04, 1.48, 1.01, 0.44, 0.00, 0.00, -0.47, -1.07, -1.53, -2.04, -2.51, -3.04))
I595_arr=np.array((3.02, 2.55, 2.02, 1.54, 1.00, 0.54, 0.00, 0.00, -0.45, -1.01, -1.52, -2.01, -2.54, -3.00))

d_theta440=np.zeros(len(theta440_arr)) + 0.1*180/np.pi
d_theta580=np.zeros(len(theta580_arr)) + 0.1*180/np.pi #Bestemt ut i fra visibilitet
d_theta595=np.zeros(len(theta595_arr)) + 0.1*180/np.pi

d_I440=np.zeros(len(I440_arr)) + 0.01  
d_I580=np.zeros(len(I580_arr)) + 0.01 #Bestemt ut i fra datablad til stromkilden
d_I595=np.zeros(len(I595_arr)) + 0.01

"""
lambda_arr=np.array((440, 580, 595))*10**9 #m
B=np.array(())
I=np.array(())
L=

def V(lambda_, theta, L, B):
	return theta/(L*B)

print V(lambda_arr[0], theta440_arr, 


plt.errorbar(I440_arr, theta440_arr, xerr=d_I440, yerr=d_theta440, fmt="k.", label="Angles measured")
plt.xlabel("Current, I, [A]")
plt.ylabel("Angle, $\\theta$, $[^o]$")
plt.title("Angle versus Current graph with $\\lambda = 440nm$")
plt.grid()
plt.legend(loc="best")
plt.show()

plt.errorbar(I580_arr, theta580_arr, xerr=d_I580, yerr=d_theta580, fmt="k.", label="Angles measured")
plt.xlabel("Current, I, [A]")
plt.ylabel("Angle, $\\theta$, $[^o]$")
plt.title("Angle versus Current graph with $\\lambda = 580nm$")
plt.grid()
plt.legend(loc="best")
plt.show()

plt.errorbar(I595_arr, theta595_arr, xerr=d_I595, yerr=d_theta595, fmt="k.", label="Angles measured")
plt.xlabel("Current, I, [A]")
plt.ylabel("Angle, $\\theta$, $[^o]$")
plt.title("Angle versus Current graph with $\\lambda = 595nm$")
plt.grid()
plt.legend(loc="best")
plt.show()
"""
I = np.array([1.0,1.5,2.0,2.5,3.0])
B = np.array([43,63,83,102,119])*1e-3

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
    #plt.plot(x,y,'bo')
    #plt.plot(x,yline)

    return m,dm,c,dc,yline

m,dm,c,dc,yline = lin(I,B,1)
L = 0.1
LB440_arr = (m*I440_arr + c)*L*10000*100 # cm * G
LB580_arr = (m*I580_arr + c)*L*10000*100
LB595_arr = (m*I595_arr + c)*L*10000*100

def linplot(x,y,i):
    deg = 1
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
    plt.title('$\lambda = %i nm$, V = %3.3e [$rad \cdot m^{-1}T^{-1}$]' % (i,m))
    plt.plot(x,y,'bo',label='datapunkter')
    plt.plot(x,yline,label='linjetilpasning')
    plt.xlabel(r'$LB [T\cdot m]$')
    plt.ylabel(r'$\theta [rad]$')
    plt.grid()
    plt.legend()
    plt.show()
    return m


m440 = linplot(LB440_arr,theta440_arr,440)
m580 = linplot(LB580_arr,theta580_arr,580)
m595 = linplot(LB595_arr,theta595_arr,595)
l = [440,580,595]
V = [m440,m580,m595]
plt.plot(l,V,'ro')
plt.xlabel(r'$\lambda [nm]$')
plt.ylabel('Verdet constant')
plt.grid()
plt.show()

