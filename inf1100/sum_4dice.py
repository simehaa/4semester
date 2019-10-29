from __future__ import division
import numpy as np
import sys

try: # try-except block, convenient for cml arguments
    r = float(sys.argv[1]) # profit per win
    N = int(sys.argv[2]) # number of experiments
except IndexError:
    print 'please provide exactly 2 cml arguments'
    sys.exit(1)
except ValueError:
    print 'please provide r reward for each game(int/float) and N number of experiments(int)'
    sys.exit(1)

m = 0 # money counter
for k in range(N):
    t = np.random.randint(1,7,4) # one throw of 4 dice
    if np.sum(t) < 9:
        m += r
    m -= 1

print 'with reward %g, profit per game: %f' % (r,(m/N)) # m/N is total profit divided by number of games

"""
simen@simen-VirtualBox:~/python/uke11$ python sum_4dice.py 10 100000
with reward 10, profit per game: -0.399510
"""
