import numpy as np
import matplotlib.pyplot as plt


n = 100
a = 0.8
b = 2.7
t = 0.5
I = 10

x1 = np.linspace(1e-10,a,n)
x2 = np.linspace(a,b,n)
x3 = np.linspace(b,b+t,n)
x4 = np.linspace(b+t,b+3*t,n)

def f1(r):
    return 2*1e-7*I/(r)*r**2/a**2

def f2(r):
    return 2*1e-7*I/(r)

def f3(r):
    return 2*1e-7*I/(r)*(1 - (r**2 - b**2)/(2*b*t + t**2))


plt.plot(x1,1e3*f1(x1))
plt.plot(x2,1e3*f2(x2))
plt.plot(x3,1e3*f3(x3))
plt.plot(x4,np.zeros(n))
plt.title('Magnetfeltstyrke |B| som funksjon av radius')
plt.plot((a,a),(0,2.5e-3),'k--')
plt.plot((b,b),(0,2.5e-3),'k--')
plt.plot((b+t,b+t),(0,2.5e-3),'k--')
plt.xlabel('r [mm], a = 0.8 mm, b = 2.7 mm, t = 0.5 mm')
plt.ylabel('B(r) [Tesla]')
plt.grid(True)
plt.show()
