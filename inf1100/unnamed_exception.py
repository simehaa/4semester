import sys
try:
    C = float(sys.argv[1])
except IndexError:
    print "Provide something in cml"   # empty cml
    sys.exit(1)
except ValueError:            # kicks in for example when string is the input
    print "Invalid"
    sys.exit(1)
