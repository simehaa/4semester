F = raw_input("How many fahrenheit? ")
F = float(F)

if F < -459.67:
    F = 'undefined'
    print 'this temperature is too low'
else:
    C = (F - 32)*5./9
    print "is %.2f degrees Celsius" % C
