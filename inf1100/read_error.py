import matplotlib.pyplot as plt
import numpy as np
import re

infile = open('error.dat','r')
epsilon = []
error = []
n = []
for line in infile:
    line = re.sub('[,:]', '', line) # re.sub swithes everthing thats in the
    line = re.sub('[=]', ' ', line) # first argument with the second argument
    words = line.split()
    epsilon.append(words[1]) # index 1 now refers to epsilon
    error.append(words[4])   # index 4 is error
    n.append(words[-1])      # the last index is n
infile.close()

eps = np.asarray(epsilon)    # array of eps and err
err = np.asarray(error)
n = np.asarray(n)

plt.title('read error from a file')
plt.plot(n,eps, label='epsilon')         # plot of error and epsilon for each n
plt.plot(n,err, label='absolute error')
plt.xlabel('n')
plt.yscale('log') # logaritmic axis scale on the y axis
plt.legend()
plt.show()

"""
simen@simen-VirtualBox:~/python/uke8$ python read_error.py

"""
