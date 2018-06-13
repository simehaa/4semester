import sys              # the module for writing arguments i the command line

t  = float(sys.argv[1]) # first command line argument
v0 = float(sys.argv[2]) # second command line argument
g  = 9.81               # g for the formula

y = v0*t - 0.5*g*t**2   # the formula
print y

"""
simen@simen-VirtualBox:~/python/uke4$ python ball_cml.py 3 15
0.855
"""
