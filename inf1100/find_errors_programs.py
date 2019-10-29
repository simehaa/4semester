from math import pi, sin, cos
x = pi/4
val_1 = (sin(x))**2 + (cos(x))**2
print val_1
# "pi" was not imported
#  sin and cos was written as math.sin and math.cos (wrong when we imported "from math")
# val was in lowercase letters, and the in uppercase letters
# 1_val started with a number, I changed it to val_1
# squared was written as sin 'normal to the power of 2', it must be **2
v0 = 3.0 # m/s
t = 1.0  # s
a = 2.0  # m/s**2
s = v0*t + 0.5*a*t**2
print s
# every value was written as integers, doesn't work well in physics
# units was not written as comments, fucks up variables
#  . for times instead of *
a = 3.3; b = 5.3
a2 = a**2
b2 = b**2

eq1_sum = a2 + 2*a*b + b2
eq2_sum = a2 - 2*a*b + b2

eq1_pov = (a + b)**2
eq2_pov = (a - b)**2

print 'First equation: %g = %g' % (eq1_sum, eq1_pov)
print 'Second equation: %g = %g' % (eq2_sum, eq2_pov)
# to variables a and b in one line needs to be separated with ;
# . for comma not ,
# 2ab must be 2*a*b
# %h whats that?
