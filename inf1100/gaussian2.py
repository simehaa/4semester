n = 10        # range for values (I choose from -5 to 5)
x_list = []   # list for x values
f_list = []   # list for f(x) values

def gauss(x,m=0,s=1):
    from math import sqrt, pi, exp   # need this for the function
    for i in range(n + 1):           # loop
        f = 1./(sqrt(2.*pi)*s)*exp((-1./2)*((x-m/s))**2) # the gaussian function
        x_list.append(x)
        f_list.append(f)
        x += 1
    for a, b in zip(x_list, f_list):
        print "%3.f | %.4g" % (a, b) # zip print for i nice table

print '__x_|_f(x)_____'  # headline print
gauss(-5,m=0,s=1)

"""
simen@simen-VirtualBox:~/python/uke3$ python gaussian2.py
__x_|_f(x)_____
 -5 | 1.487e-06
 -4 | 0.0001338
 -3 | 0.004432
 -2 | 0.05399
 -1 | 0.242
  0 | 0.3989
  1 | 0.242
  2 | 0.05399
  3 | 0.004432
  4 | 0.0001338
  5 | 1.487e-06
""" 
# the final program, I can see that the max value is at 0
# and that the values mirror on both sides from 0, as expected
# for a gaussian function
