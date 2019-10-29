import numpy as np
import matplotlib.pyplot as plt

infile = open('maalinger_deformasjon.dat','r')
x,y = [],[]
for line in infile:
    a = line.split()
    x.append(eval(a[0]))
    y.append(eval(a[1]))
infile.close()
x = np.array(x)
y = np.array(y)

def solve_least_square_polynomial(degree,xdata,ydata,n):
    X = np.zeros((n,degree + 1))
    for i in range(degree + 1):
        X[:,i] = xdata**i
    XT = np.matrix.transpose(X)
    XTX = np.matmul(XT,X)
    XTy = np.matmul(XT,ydata)
    XTX_inv = np.linalg.inv(XTX)
    return np.matmul(XTX_inv,XTy)


def solve_least_square_sin_cos(xdata,ydata,n):
    X = np.zeros((n,2))
    X[:,0] = np.sin(2*np.pi*xdata)
    X[:,1] = np.cos(2*np.pi*xdata)
    XT = np.matrix.transpose(X)
    XTX = np.matmul(XT,X)
    XTy = np.matmul(XT,y)
    XTX_inv = np.linalg.inv(XTX)
    return np.matmul(XTX_inv,XTy)


def plot_least_square_polynomial(degree,xdata,ydata,n):
    B = solve_least_square_polynomial(degree,xdata,ydata,n)
    print B[1]
    def f(degree,B,x):
        s = 0
        for i in range(degree + 1):
            s += B[i]*x**i
        return s
    t = np.linspace(np.min(xdata),np.max(xdata),100)
    plt.title('minste kvadraters losning med polynom av grad %i' % degree)
    plt.plot(t,f(degree,B,t))
    plt.plot(xdata,ydata,'ko')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid()
    plt.show()
    e = np.zeros(n)
    for i in range(n):
        e[i] = abs(ydata[i] - f(degree,B,xdata[i]))
    return e


def plot_least_square_sin_cos(xdata,ydata,n):
    B = solve_least_square_sin_cos(xdata,ydata,n)
    def g(B,x):
        return B[0]*np.sin(2*np.pi*x) + B[1]*np.cos(2*np.pi*x)
    m = np.min(xdata)
    M = np.max(xdata)
    l = M-m
    t = np.linspace(m-2*l,m+2*l,100)
    plt.title('minste kvadraters losning med sinus/cosinus-funksjon')
    plt.plot(t,g(B,t))
    plt.plot(xdata,ydata,'ko')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid()
    plt.show()
    e = np.zeros(n)
    for i in range(n):
        e[i] = abs(ydata[i] - g(B,xdata[i]))
    return e

n = len(x)
p = np.polyfit(x,y,1)
yline = np.polyval(p,x)
m = p[0]
c = p[1]
D = np.sum(x*x) - (np.sum(x))**2/n
E = np.sum(x*y) - np.sum(x)*np.sum(y)/n
F = np.sum(y*y) - (np.sum(y))**2/n
dm = np.sqrt((1./(n - 2))*(D*F - E**2)/D**2)
dc = np.sqrt((1./(n - 2))*(D/n + (np.mean(x))**2)*((D*F - E**2)/D**2))
# S = 0
# for i in range(n):
    # S += abs(y[i] - yline[i])**2
# dm = 1./(n-2)
plt.plot(x,y,'ko')
plt.plot(x,yline,'b-')
plt.xlabel('masse [kg]')
plt.ylabel('utslag [mm]')
plt.grid(True)
plt.show()
print "m = %.3f" % m
print "dm = %g" % dm

# e = plot_least_square_polynomial(1,x,y,len(x))
