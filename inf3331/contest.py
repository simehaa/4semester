import numpy as np

def f1(x): # missing constant 15/pi
    return np.sin(x)*np.sin(x/3.)*np.sin(x/5.)/x**3

def f2(x): # missing constant 105/pi
    return np.sin(x)*np.sin(x/3.)*np.sin(x/5.)*np.sin(x/7.)/x**4

def f6(x): # missing constant 945/pi
    return np.sin(x)*np.sin(x/3.)*np.sin(x/5.)*np.sin(x/7.)*np.sin(x/9.)/x**5

def f3(x): # missing constant 10395/pi
    return np.sin(x)*np.sin(x/3.)*np.sin(x/5.)*np.sin(x/7.)*np.sin(x/9.)*np.sin(x/11.)/x**6

def f4(x): # missing constant 135135/pi
    return np.sin(x)*np.sin(x/3.)*np.sin(x/5.)*np.sin(x/7.)*np.sin(x/9.)*np.sin(x/11.)*np.sin(x/13.)/x**7

def f5(x): # missing constant 2027025/pi
    return np.sin(x)*np.sin(x/3.)*np.sin(x/5.)*np.sin(x/7.)*np.sin(x/9.)*np.sin(x/11.)*np.sin(x/13.)*np.sin(x/15.)/x**8


def integrate(a,b,f,n): # the trapezoidal method
    x = np.linspace(a,b,int(n))
    s = np.sum(f(x)) 
    s -= (f(a) + f(b))*0.5
    s *=(b-a)/(n)
    return s

#print(integrate(1e-20,1e7,f1,1e8)*15/np.pi)      # print: 0.499999995
#print(integrate(1e-20,1e7,f2,1e7)*105/np.pi)     # print: 0.49999995
#print(integrate(1e-20,1e7,f6,1e7)*945/np.pi)     # print: 0.49999995
#print(integrate(1e-20,1e7,f3,1e7)*10395/np.pi)   # print: 0.49999995
#print(integrate(1e-20,1e7,f4,1e7)*135135/np.pi)  # print: 0.49999995
#print(integrate(1e-20,1e7,f5,1e7)*2027025/np.pi) # print: 0.499999949993