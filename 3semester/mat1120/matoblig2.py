import numpy as np
import matplotlib.pyplot as plt

infile = open('labdata.txt','r')
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

n = 4 # number of data points
x = np.zeros(n)
x[0] = 0.08
x[1] = 0.12
x[2] = 0.2
x[3] = 0.38
y = np.zeros(n)
y[0] = 4.05
y[1] = 4.15
y[2] = 3.85
y[3] = -0.22
degree = 2

e1 = plot_least_square_polynomial(degree,x,y,n)
e2 = plot_least_square_sin_cos(x,y,n)

average_error_f = np.sum(e1)/float(n)
average_error_g = np.sum(e2)/float(n)
if average_error_f < average_error_g:
    print "f(x) = polynomial of degree %i, was better than g(x) = a sin(2pix) + b cos(2pix)" % degree
else:
    print "g(x) = a sin(2pix) + b cos(2pix), was better than f(x) = polynomial of degree %i" % degree

"""
[Command: python -u /home/simen/matoblig2.py]
f(x) = polynomial of degree 2, was better than g(x) = a sin(2pix) + b cos(2pix)
[Finished in 7.677s]
"""
