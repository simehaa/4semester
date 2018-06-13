from __future__ import division
import numpy as np
import sys

try: # try-except block, convenient for cml arguments
    n = int(sys.argv[1]) # number of dice
    e = int(sys.argv[2]) # number of experiments
except IndexError:
    print 'please provide exactly 2 cml arguments'
    sys.exit(1)
except ValueError:
    print 'please provide integers'
    sys.exit(1)

for i in range(1,n + 1):
    c = 0
    for k in range(e):
        throw = np.random.randint(1,7,i) # random int from 1 to 6, length of array = number of dice
        no_six = throw[throw<6] # no_six is an array, where '6' was not present in throw
        if len(no_six) == i: # simply checking if this throw had a '6' in it
            c += 1 # counting how many throws which had no '6'
    p = 1 - c/e # total probability: (1 - c/e) = at least one '6'
    print '%i dice - probability = %.4f' % (i,p)

# these results makes sense, roughly 1/6 (0.1666) for 1 dice,
# 11/36 (0.3055...) for 2 dice, and increasing probability
"""
simen@simen-VirtualBox:~/python/uke11$ python one6_ndice.py 5 10000
1 dice - probability = 0.1632
2 dice - probability = 0.3057
3 dice - probability = 0.4182
4 dice - probability = 0.5205
5 dice - probability = 0.5916
"""
