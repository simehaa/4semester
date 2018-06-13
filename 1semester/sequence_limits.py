import numpy as np
import matplotlib.pyplot as plt

N = 80
an = np.zeros(N)
s_ = np.zeros(N)
D_ = np.zeros(N)
x_ = np.zeros(N)

def seq():
    for n in range(len(an)):
        teller = float(8/(n + 1))
        nevner = 2./((n+1)**2)
        an[n] = teller/nevner
    return an

# print seq()

def seq2():
    for n in range(len(s_)):
        s_[n] = (np.sin(2**(-n))/(2**(-n)))
    return s_

# print seq2()

def D(x):
    def f(k):
        return np.sin(k)
    for n in range(len(D_)):
        h = (2**(-n))
        D_[n] = float(f(x+h) - f(x))/float(h)
        print (float(f(x+h) - f(x))), h
    plt.plot(x_,D_,'ro')
    plt.show()


D(np.pi)
