# 7.11
from math import exp, sin

class F:
    def __init__(self, a, w):
        self.a = a
        self.w = w

    def __call__(self, x): # when calling for f as a function (f(argument)), this method will be called
        return exp(-self.a*x)*sin(self.w*x)

    def __str__(self): # when asking for the function itself (print f), this string will be printed showing the function
        return 'exp(-a*x)*sin(w*x)'


# I wrote "from F2 import ... instead of from F like in the task, because the filename was F2"
"""
simen@simen-VirtualBox:~/python/uke9$ python
Python 2.7.12 (default, Jul  1 2016, 15:12:24)
[GCC 5.4.0 20160609] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> from F2 import F
>>> f = F(a=1.0, w=0.1)
>>> from math import pi
>>> print f(x=pi)
0.013353835137
>>> f.a = 2
>>> print f(pi)
0.00057707154012
>>> print f
exp(-a*x)*sin(w*x)
>>>
"""
