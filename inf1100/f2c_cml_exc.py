import sys

try:
    F = float(sys.argv[1])
except:
    print 'please provide a Fahrenheit value'
    F = float(raw_input('F = '))

if F < -459.67:
    F = 'undefined'
    print 'this temperature is too low'
else:
    C = (F - 32)*5/9.
    print "is %.2f degrees Celsius" % C
