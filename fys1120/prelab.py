import numpy as np
import matplotlib.pyplot as plt
import sys
degree = sys.argv[1]
"""
infile = open('labdata.txt','r')
x,y = [],[]
for line in infile:
    a = line.split()
    x.append(eval(a[0]))
    y.append(sum([eval(i) for i in a[1:]])/(len(a[1:])))
infile.close()
x = np.array(x)
y = np.array(y)


b = np.polyfit(x,y,degree)
t = np.linspace(np.min(x),np.max(x),100)
integral = np.trapz(np.polyval(b,t),t,0.01)
B = integral/float(2*11)
plt.plot(t,np.polyval(b,t))
plt.plot(x,y,'ko')
plt.title('B = %2.1e' % B)
plt.xlabel('time [s]')
plt.ylabel('emf [V]')
plt.grid()
plt.show()


infile = open('oppg1.txt','r')
x,y = [],[]
for line in infile:
    a = line.split()
    x.append(eval(a[0]))
    y.append(eval(a[1]))
infile.close()
x = np.array(x)
y = np.array(y)
plt.plot(x,y)
plt.xlabel('time [s]')
plt.ylabel('potensial [V]')


tau = np.zeros(len(x))
for i in range(len(x)):
    tau[i] = x[i]/(-np.log(y[i]/9.0))

Tau = np.average(tau)
R = Tau/8.3e-6
dev = 0
for i in range(len(x)):
    dev += abs(tau[i] - Tau)
stddev = dev/(len(tau))
plt.title('Tau = %2.0f +- %2.1f s' % (Tau,stddev))
plt.grid()
plt.show()

infile = open('oppg2.txt','r')
x,y = [],[]
for line in infile:
    a = line.split()
    x.append(eval(a[0]))
    y.append(eval(a[1]))
infile.close()
x = np.array(x)
y = np.array(y)
plt.plot(x,y)
b = np.polyfit(x,y,degree)
t = np.linspace(np.min(x),np.max(x),100)
plt.plot(t,np.polyval(b,t))
plt.plot(x,y,'ko')
plt.xlabel('current [mA]')
plt.ylabel('potensial [mV]')
plt.title('R = %2.0f Ohm' % b[0])
plt.grid()
plt.show()
"""
infile = open('oppg3.txt','r')
x,y = [],[]
for line in infile:
    a = line.split()
    x.append(eval(a[0]))
    y.append(eval(a[1]))
infile.close()
x = np.array(x)
y = np.array(y)
b = np.polyfit(x,y,degree)
t = np.linspace(np.min(x),np.max(x),100)
plt.plot(t,np.polyval(b,t),label='graph')
plt.plot(x,y,'ko',label='data')
plt.legend()
plt.xlabel('Resistance [Ohm]')
plt.ylabel('potensial [V]')
plt.grid()
plt.title('I = %.3f A' % b[0])
plt.show()
