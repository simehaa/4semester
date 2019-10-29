from __future__ import division
import numpy as np

index_set = [1,2,4,6]
for i in index_set:
    N = 10**i
    r = np.random.random(N) # size N
    r1 = r[r>0.5] # all numbers higher than 0.5
    r1 = r1[r1<0.6] # all numbers also lower than 0.6
    print '10**%i iterations - probability: %.4f' % (i, len(r1)/N) # probability = M/N

"""
[Command: python -u /home/simen/python/uke11/compute_prob_vec.py]
10**1 iterations - probability: 0.1000
10**2 iterations - probability: 0.0800
10**4 iterations - probability: 0.1017
10**6 iterations - probability: 0.1001
[Finished in 0.146s]
"""
