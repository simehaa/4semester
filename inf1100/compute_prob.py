from __future__ import division
import random

M = 0 # counter
index_set = [1,2,3,6]
for i in index_set:
    N = 10**i # number of iterations
    for j in range(N):
        number = random.random() #random number in interval [0,1)
        if 0.5 < number < 0.6:
            M += 1
    print '10**%i iterations - probability: %.4f' % (i, M/N) # probability = M/N

"""
[Command: python -u /home/simen/python/uke11/compute_prob.py]
10**1 iterations - probability: 0.0000
10**2 iterations - probability: 0.0900
10**3 iterations - probability: 0.1030
10**6 iterations - probability: 0.1002
[Finished in 0.22s]
"""
