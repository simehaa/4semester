# Exercise 1.10: Evaluate a Gaussian function
m = 0.0 # a real number
s = 2.0 # a real number
x = 1.0
from math import sqrt, pi, exp # importing the necessary functions from the math module
y = 1/((sqrt(2.*pi))*s) *exp(- 1.0/2*((x - m)/s)**2) # the Gaussian function
print """The Gaussian function when
m = %.f
s = %.f
x = %.f

gives the result
f(x) = %.12f""" % (m, s, x, y)

"""
simen@simen-VirtualBox:~/python/uke1$ python gaussian1.py
The Gaussian function when
m = 0
s = 2
x = 1

gives the result
f(x) = 0.176032663382
"""
