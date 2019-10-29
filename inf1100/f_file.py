infile = open('temperature.dat','r')

infile.readline()
infile.readline()
infile.readline()

line = infile.readline()
print line

F = float(F)
C = (F - 32)*5./9

print "%g degrees F is %1.f degrees C" % (F,C)
