import matplotlib.pyplot as plt
import numpy as np

# a) and b) series of aj and sj implemented in a function

def cos_Taylor(x, n):
    s = 0
    a = 1.0
    for i in range(1, n + 2):             # difference equation without using arrays
        s += a                            # I think this is the best way, because the
        a *= -x**2/float((2*i - 1)*(2*i)) # program doesn't save all values, and takes less memory
    return s, abs(a)

# c) test function

def test_cos_Taylor():  # test function for cos_Taylor(1,2)
    # x = 1, n = 2
    expected = 1 - 1./2 + 1./24
    computed = cos_Taylor(1, 2)[0]
    tol = 1e-14
    success = abs(expected - computed) < tol
    msg = 'function failed, expected %.16f got %.16f' % (expected, computed)
    assert success, msg

test_cos_Taylor()

# d) plot

x = np.linspace(-4*np.pi, 4*np.pi, 301)              # plot of s
plt.plot(x, cos_Taylor(x,14)[0],'b-',label='n = 13') # the plot showed that the accuracy improved
plt.plot(x, cos_Taylor(x,11)[0],'k-',label='n = 10') # when n increased and when x decreased
plt.plot(x, cos_Taylor(x,8)[0], 'r-',label='n = 7' )
plt.plot(x, cos_Taylor(x,5)[0], 'y-',label='n = 3' )
plt.plot(x, cos_Taylor(x,2)[0], 'g-',label='n = 2' )
plt.plot(x, cos_Taylor(x,14)[1],'bo',label='absolute error') # plot of a, just to illustrate the
plt.plot(x, cos_Taylor(x,11)[1],'ko',label='absolute error') # absoulute error for each previous graph
plt.plot(x, cos_Taylor(x,8)[1] ,'ro',label='absolute error')
plt.plot(x, cos_Taylor(x,5)[1] ,'yo',label='absolute error')
plt.plot(x, cos_Taylor(x,2)[1] ,'go',label='absolute error')
plt.axis([-15,30,-2,2])
plt.title('Taylor series of cos(x) with increasing n')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

"""
simen@simen-VirtualBox:~/python/uke8$ python cos_Taylor_series_diffeq.py

"""
