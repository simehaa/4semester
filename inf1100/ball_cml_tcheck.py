import sys              # the module for writing arguments i the command line

t  = float(sys.argv[1]) # first command line argument
v0 = float(sys.argv[2]) # second command line argument
g  = 9.81               # g for the formula
limit = 2*v0/g

if t < 0 or t > limit:
    print 't value not valid, t must be between 0 and 2*v0/g'
    print 'the ball is not in the air!'
    sys.exit(1)

y = v0*t - 0.5*g*t**2   # the formula
print y

"""
simen@simen-VirtualBox:~/python/uke4$ python ball_cml_tcheck.py 45 2
t value not valid, t must be between 0 and 2*v0/g
the ball is not in the air!
"""
