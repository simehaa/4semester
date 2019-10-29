t  = raw_input("t = "); t  = float(t)    # asks user for t
v0 = raw_input("v0 = "); v0 = float(v0)  # asks user for initial velocity
g = 9.81                                 # g for the formula
y = v0*t - 0.5*g*t**2                    # the formula
print y

"""
simen@simen-VirtualBox:~/python/uke4$ python ball_qa.py
t = 2
v0 = 10
0.38
"""
