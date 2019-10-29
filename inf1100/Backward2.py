from Diff import Diff # Diff file from all book files

class Backward1(Diff):
    def __call__(self, x):
        f, h = self.f, self.h
        return (f(x) - f(x - h))/h

class Backward2(Diff):
    def __call__(self, x):
        f, h = self.f, self.h
        return (f(x - 2*h) - 4*f(x - h) + 3*f(x))/(2*h) # Backward2 function


from math import exp
exact = exp(0)
t = 0
for k in range(15):
    f = exp
    h = 2**(-k)
    b1 = Backward1(f,h)
    b2 = Backward2(f,h)
    approx1 = b1(0)
    approx2 = b2(0)
    error1 = abs(exact - approx1)
    error2 = abs(exact - approx2)
    print 'h = 2**(-%2i): derivative Backward1 = %.8f, error = %.8e \
          \n              derivative Backward2 = %.8f, error = %.8e' % (k, approx1, error1, approx2, error2)


# this print indicates that the Backward2 approaches a smaller error quicker than Backward1
"""
simen@simen-VirtualBox:~/python/uke10$ python Backward2.py
h = 2**(- 0): derivative Backward1 = 0.63212056, error = 3.67879441e-01
              derivative Backward2 = 0.83190876, error = 1.68091241e-01
h = 2**(- 1): derivative Backward1 = 0.78693868, error = 2.13061319e-01
              derivative Backward2 = 0.94175680, error = 5.82431977e-02
h = 2**(- 2): derivative Backward1 = 0.88479687, error = 1.15203132e-01
              derivative Backward2 = 0.98265505, error = 1.73449451e-02
h = 2**(- 3): derivative Backward1 = 0.94002478, error = 5.99752207e-02
              derivative Backward2 = 0.99525269, error = 4.74730907e-03
h = 2**(- 4): derivative Backward1 = 0.96939099, error = 3.06090050e-02
              derivative Backward2 = 0.99875721, error = 1.24278935e-03
h = 2**(- 5): derivative Backward1 = 0.98453650, error = 1.54635032e-02
              derivative Backward2 = 0.99968200, error = 3.18001470e-04
h = 2**(- 6): derivative Backward1 = 0.99222803, error = 7.77196835e-03
              derivative Backward2 = 0.99991957, error = 8.04334493e-05
h = 2**(- 7): derivative Backward1 = 0.99610390, error = 3.89609731e-03
              derivative Backward2 = 0.99997977, error = 2.02262762e-05
h = 2**(- 8): derivative Backward1 = 0.99804942, error = 1.95058435e-03
              derivative Backward2 = 0.99999493, error = 5.07138901e-06
h = 2**(- 9): derivative Backward1 = 0.99902407, error = 9.75927027e-04
              derivative Backward2 = 0.99999873, error = 1.26970485e-06
h = 2**(-10): derivative Backward1 = 0.99951188, error = 4.88122343e-04
              derivative Backward2 = 0.99999968, error = 3.17658760e-07
h = 2**(-11): derivative Backward1 = 0.99975590, error = 2.44100893e-04
              derivative Backward2 = 0.99999992, error = 7.94439075e-08
h = 2**(-12): derivative Backward1 = 0.99987794, error = 1.22060379e-04
              derivative Backward2 = 0.99999998, error = 1.98642738e-08
h = 2**(-13): derivative Backward1 = 0.99993897, error = 6.10326724e-05
              derivative Backward2 = 1.00000000, error = 4.96584107e-09
h = 2**(-14): derivative Backward1 = 0.99996948, error = 3.05169578e-05
              derivative Backward2 = 1.00000000, error = 1.24418875e-09
"""
