from __future__ import division
import numpy as np

def exact(eyes):
    die = [1, 2, 3, 4, 5, 6]
    a = 0
    for i in range(6):
        for k in range(6): # total of 36 loops, counting 1+1,1+2...2+1...6+6
            s = die[i] + die[k]
            if s == eyes:
                a += 1
    return a/36. # return the exact probability to get a
                 # specific number of eyes on a two dice throw

n = 1000000
t1 = np.random.randint(1,7,n)
t2 = np.random.randint(1,7,n)
t = t1 + t2 # t1 and t2 are two 1 die throws (n times), t is one 2 dice throws (n times)
print '_eyes_|_frequency__|_probability_'
for i in range(2,13):
    a = t[t==i] # checking how many of the throws that had i eyes
    print ' %2i   |   %6i   |   %.4f' % (i, len(a), exact(i))

"""
[Command: python -u /home/simen/python/uke11/freq_2dice.py]
_eyes_|_frequency__|_probability_
  2   |    28165   |   0.0278
  3   |    55393   |   0.0556
  4   |    84008   |   0.0833
  5   |   111776   |   0.1111
  6   |   138737   |   0.1389
  7   |   166324   |   0.1667
  8   |   138571   |   0.1389
  9   |   110751   |   0.1111
 10   |    82845   |   0.0833
 11   |    55671   |   0.0556
 12   |    27759   |   0.0278
[Finished in 0.207s]
"""
