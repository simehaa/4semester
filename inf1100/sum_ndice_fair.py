from __future__ import division
import numpy as np

N = 100000 # number of experiments to estimate the probability
s = 9 # get less than this sum to win a game
n = 4 # dice
q = 1 # [euros] cost

def probability(s, n, N):
    l = 0
    for i in range(N):
        a = np.random.randint(1,7,n) # a throw of n dice
        if np.sum(a) < s:
            l += 1 # counting how many of throws that got less than s eyes
    return l/N # probability estimate

award = q/probability(s, n, N)
print 'this game is fair with an award of %.4f euros' % award

# estimate of the fair award:
"""
[Command: python -u /home/simen/python/uke11/sum_ndice_fair.py]
this game is fair with an award of 18.5219 euros
[Finished in 1.486s]
"""
# test of this award on exercise 8.8 sum_4dice.py
"""
simen@simen-VirtualBox:~/python/uke11$ python sum_4dice.py 18.5219 100000
with reward 18.5219, profit per game: 0.002220
"""
