import sys              # the module for writing arguments i the command line

g = 9.81                # g for the formula

try:
    t = float(sys.argv[1])
except:
    print 'you must provide a float as an input for time'
    t  = float(raw_input("t = "))

try:
    v0 = float(sys.argv[2])
except:
    print 'you must provide a float as an input for initial velocity'
    v0 = float(raw_input("v0 = "))

y = v0*t - 0.5*g*t**2   # the formula
print y

"""
simen@simen-VirtualBox:~/python/uke4$ python ball_cml.py hei du
you must provide a float as an input for time
t = 2
you must provide a float as an input for initial velocity
v0 = 15
10.38
"""
